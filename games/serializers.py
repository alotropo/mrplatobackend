from dataclasses import fields
from rest_framework import serializers

from .models import ListQuestionGame,QuestionGame


class ListGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListQuestionGame
        fields = "__all__"


class QuestionGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionGame
        fields = "__all__"