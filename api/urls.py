
from unicodedata import name
from django.urls import path,include,re_path
from rest_framework import routers

from .views import ApiContent, ApiNotification, ApiTest, ListExerciseView,api_test,ApiQuestionExercise

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r"content",ApiContent)


urlpatterns = [
    path("",ApiTest.as_view(),name="test"),
    path("",include(router.urls)),
    path("notification/",ApiNotification.as_view(),name="notification"),
    path("list-exercise/",ListExerciseView.as_view({"get":"list"}),name="list"),
    re_path("list-exercise/question/(?P<id>.+)/$",ApiQuestionExercise.as_view(),name="exercise")
    
]
