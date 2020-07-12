from rest_framework.generics import ListAPIView

from home.models import Banner, Nav,Footer
from home.serializers import BannerModelSerializer, NavModelSerializer,FooterModelSerializer
from edu_api.settings.constants import BANNER_LENGTH, NAV_LENGTH,FOOTER_NAV_LENGTH


class BannerListAPIView(ListAPIView):
    """轮播图"""
    queryset=Banner.objects.filter(is_show=True, is_delete=False).order_by("-orders")[:BANNER_LENGTH]
    serializer_class=BannerModelSerializer


class HeaderListAPIView(ListAPIView):
    """导航菜单"""
    queryset=Nav.objects.filter(is_show=True, is_delete=False).order_by("-orders")[:NAV_LENGTH]
    serializer_class=NavModelSerializer


class FooterNavListAPIView(ListAPIView):
    queryset=Footer.objects.filter(is_show=True, is_delete=False, position=2).order_by('orders')[:FOOTER_NAV_LENGTH]
    serializer_class=FooterModelSerializer
