from rest_framework import serializers
from .models import ListExercise

class ListExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListExercise
        fields = "__all__"