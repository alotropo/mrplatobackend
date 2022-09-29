from email.policy import default
from django.db import models

# Create your models here.


class Question(models.Model):
    text = models.TextField()
    result = models.TextField()
    category = models.CharField(max_length=50)
    data_created = models.DateField(auto_now=True)
    resolution = models.TextField()


class ListExercise(models.Model):
    list_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    availability = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.list_name
    

    class Meta:
        ordering = ('-availability', )