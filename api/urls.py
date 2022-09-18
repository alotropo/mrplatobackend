
from django.urls import path
from rest_framework import routers

from .views import ApiTest,api_test



urlpatterns = [
    path("",ApiTest.as_view(),name="test"),
]
