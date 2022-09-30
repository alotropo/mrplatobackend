from dataclasses import fields
from rest_framework import serializers
from .models import ListExercise, Question

class ListExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListExercise
        fields = "__all__"

class QuestionExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"