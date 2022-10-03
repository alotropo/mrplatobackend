from dataclasses import fields
from rest_framework import serializers
from .models import ListExercise, Question,ListChallenge,QuestionChallenge

class ListExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListExercise
        fields = "__all__"

class QuestionExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class ListChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListChallenge
        fields = "__all__"


class QuestionChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionChallenge
        fields = "__all__"
