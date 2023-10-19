from django.urls import path
from .views import *

urlpatterns = [
    path("", MainPage.as_view(), name="category_detail"),
    path("home", MainPage.as_view(), name="category_detail"),
    path("<slug:cat_slug>", CategoryPage.as_view(), name='category'),
]
