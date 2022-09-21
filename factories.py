from unicodedata import category
import factory
from faker import Faker


faker = Faker()

class QuestionFactory(factory.django.DjangoModelFactory):
    text = faker.paragraph()
    result = faker.word()
    category = faker.word()
    resolution = faker.word()

    class Meta:
        model = "exercises.Question"


class NotificationFactory(factory.django.DjangoModelFactory):
    title = faker.sentences()
    text = faker.paragraph()

    class Meta:
        model = "notification.Notification"

