from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('home', views.index),
    path('', views.index),
    path('smartphones', views.smartphones),
    path('smart_watches', views.smart_watches_def),
    path('smart_speaker', views.smart_speaker),
    path('speaker', views.speaker),
    path('routers', views.routers),
    path('zala', views.zala),
    path('smart_home', views.smart_home),
    path('tv', views.tv),
    path('notebooks', views.notebooks),
    path('pads', views.pads),
    path('scooters', views.scooters),
    path('robovacum', views.robovacum),
    path('coffee', views.coffee),
    path('conditioners', views.conditioners),
    path('other', views.other),
    path('routers_rent', views.routers_rent),
    path('upu2', views.upu2),
    path('upu3', views.upu3),
    path('upu4', views.upu4),
    path('upu5', views.upu5),

]
