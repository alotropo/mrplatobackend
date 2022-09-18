from django.db import models

# Create your models here.


class Question(models.Model):
    text = models.TextField()
    result = models.TextField()
    category = models.CharField(max_length=50)
    data_created = models.DateField(auto_now=True)
    resolution = models.TextField()