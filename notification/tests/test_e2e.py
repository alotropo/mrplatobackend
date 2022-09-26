from http.client import responses
from inspect import getmodule
from notification.models import Notification
import pytest
from faker import Faker
import json
pytestmark = pytest.mark.django_db


faker = Faker()

class TestNotification:
    endpoint = "/api/v1/notification/"
    def test_status_code(self,api_client):
        response = api_client().get(self.endpoint)
        assert response.status_code == 200

    def test_list_view(self,api_client):
    
        create = Notification.objects.using("mrplatofixed").create(text=faker.paragraph)
        getmodel = Notification.objects.using("mrplatofixed").all()
        response = api_client().get(self.endpoint)
        assert getmodel.__len__() == len(json.loads(response.content ))

