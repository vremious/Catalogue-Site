from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

router = routers.DefaultRouter()
router.register(r'type', TypeViewSet, basename='type')
router.register(r'models', ModViewSet, basename='models')
router.register(r'company', CompanyViewSet, basename='company')

urlpatterns = [

    path("", MainPage.as_view(), name="category_detail"),
    path("", include(router.urls)),
    path("home", MainPage.as_view(), name="category_detail"),
    path("<slug:cat_slug>", CategoryPage.as_view(), name='category'),


]

