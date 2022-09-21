from django.db import models

# Create your models here.
class Notification(models.Model):
    title = models.TextField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title