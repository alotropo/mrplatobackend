from dataclasses import fields
from rest_framework import serializers
from .models import ListExercise, Question,ListChallenge,QuestionChallenge,QuestionTounamment,ListTournamment

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



class ListTournammentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListTournamment
        fields = "__all__"


class QuestionTournammentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionTounamment
        fields = "__all__"