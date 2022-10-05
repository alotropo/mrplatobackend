from xmlrpc.client import boolean
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class ListQuestionGame(models.Model):
    list_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    availability = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.list_name



class QuestionGame(models.Model):
    text = RichTextField()
    list = models.ForeignKey(ListQuestionGame, on_delete=models.CASCADE)
    solution = models.BooleanField()

    def __str__(self) -> str:
        return self.text

