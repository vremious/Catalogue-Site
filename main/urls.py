from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [

    # path('home', views.index),
    # path('', views.index),
    path("", MainPage.as_view(), name="category_detail"),
    path("home", MainPage.as_view(), name="category_detail"),

    # path('smartphones', views.smartphones),
    # path('smart_watches', views.smart_watches_def),
    # path('smart_speaker', views.smart_speaker),
    # path('speaker', views.speaker),
    # path('routers', views.routers),
    # path('zala', views.zala),
    # path('smart_home', views.smart_home),
    # path('tv', views.tv),
    # path('console', views.console),
    # path('cooking', views.cooking),
    # path('notebooks', views.notebooks),
    # path('pads', views.pads),
    # path('scooters', views.scooters),
    # path('bikes', views.bikes),
    # path('robovacum', views.robovacum),
    # path('coffee', views.coffee),
    # path('conditioners', views.conditioners),
    # path('other', views.other),
    # path('routers_rent', views.routers_rent),
    # path('upu2', views.upu2),
    # path('upu3', views.upu3),
    # path('upu4', views.upu4),
    # path('upu5', views.upu5),
    path("<slug:cat_slug>", CategoryPage.as_view(), name='category'),

    # path("filter/", CategoryPage.as_view(), name='filter'),



]
