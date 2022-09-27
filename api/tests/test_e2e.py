import pytest
import json
from exercises.models import Question
from commom.utils import get_question

pytestmark = pytest.mark.django_db

class TestEndPoint:
    endpoint = "/api/v1/"
    def test_status_code(self,api_client):
        response = api_client().get(self.endpoint)
        assert response.status_code == 200

    def test_create(self, api_client,create_question):
        
        expected_json = {
            'text': create_question.text,
            'result': create_question.result,
            'category': create_question.category,
            'resolution': create_question.resolution,
        }

        response = api_client().post(
            self.endpoint,
            data=expected_json,
            format='json'
        )
        
        assert json.loads(response.content) == expected_json
        assert response.status_code == 201

