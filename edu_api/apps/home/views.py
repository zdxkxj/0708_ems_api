from rest_framework.generics import ListAPIView

from home.models import Banner, Nav
from home.serializers import BannerModelSerializer, NavModelSerializer
from edu_api.settings.constants import BANNER_LENGTH, NAV_LENGTH


class BannerListAPIView(ListAPIView):
    """轮播图"""
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by("-orders")[:BANNER_LENGTH]
    serializer_class = BannerModelSerializer


class HeaderListAPIView(ListAPIView):
    """导航菜单"""
    queryset = Nav.objects.filter(is_show=True, is_delete=False).order_by("-orders")[:NAV_LENGTH]
    serializer_class = NavModelSerializer