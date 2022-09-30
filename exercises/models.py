from email.policy import default
from django.db import models

# Create your models here.

DIFF_CHOICES = (
    ('desafios', 'desafios'),
    ('lista_exercicios', 'lista_exercicios'),
    ('torneio', 'torneio'),
)



class Question(models.Model):
    category = models.CharField(max_length=50)
    text = models.TextField()
    result = models.TextField()
    data_created = models.DateField(auto_now=True)
    resolution = models.TextField()


    def __str__(self) -> str:
        return self.result


class ListExercise(models.Model):
    list_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    availability = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.list_name
    

    class Meta:
        ordering = ('-availability', )