import pytest

from exercises.models import Question



pytestmark= pytest.mark.django_db

class TestModel:
    def get_question(self):
        query = Question.objects.all()
        return list(query.values_list("text", flat=True))


        