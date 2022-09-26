from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.

class Content(models.Model):
    topic = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    text = RichTextField()
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.topic