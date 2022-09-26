
from unicodedata import name
from django.urls import path
from rest_framework import routers

from .views import ApiContent, ApiNotification, ApiTest,api_test



urlpatterns = [
    path("",ApiTest.as_view(),name="test"),
    path("content/",ApiContent.as_view(),name="content"),
    path("notification/",ApiNotification.as_view(),name="notification"),
]
