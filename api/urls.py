
from unicodedata import name
from django.urls import path,include
from rest_framework import routers

from .views import ApiContent, ApiNotification, ApiTest,api_test

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r"content",ApiContent)


urlpatterns = [
    path("",ApiTest.as_view(),name="test"),
    path("",include(router.urls)),
    path("notification/",ApiNotification.as_view(),name="notification"),
]
