import pytest

from rest_framework.test import APIClient

from factories import QuestionFactory

from django.test import TestCase

TestCase.databases={"mrplatofixed","mrplatoflexible"}



@pytest.fixture
def create_question():
    return QuestionFactory()


@pytest.fixture
def api_client():
    return APIClient