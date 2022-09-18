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
