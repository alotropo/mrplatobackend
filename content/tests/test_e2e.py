from time import sleep
from urllib import request, response
import pytest
from content.models import Content

from rest_framework.test import RequestsClient

import json

pytestmark = pytest.mark.django_db


from api.serializers import ContentSerializer


class TestEnd2End:
    endpoint = "/api/v1/content/"
    
    def test_status_code(self,api_client):

        response = api_client().get(self.endpoint)

        assert response.status_code == 200

    def test_get_content(self,api_client):
        create = Content.objects.using("mrplatofixed").create(title="kaqui")
        content = Content.objects.using("mrplatofixed").all()
        response = api_client().get(self.endpoint)
        assert len(json.loads(response.content)) == content.__len__()

    
        