import pytest

from notification.models import Notification

pytestmark = pytest.mark.django_db

class TestNotification:
    def get_notification(self):
        query = Notification.objects.all()
        return list(query.values_list("text", flat=True))


    def test_verify(self,create_notification):
        assert [create_notification.text] == self.get_notification()
