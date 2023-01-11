from django.db import models

# Create your models here.




class ConfigRate(models.Model):
    rate_exercise = models.FloatField(default=0.25)
    rate_tournamment = models.FloatField(default=0.25)
    rate_challenges = models.FloatField(default=0.25)
    rate_games = models.FloatField(default=0.25)

    total_points = models.IntegerField(default=0)

    def __str__(self):
        return "é preciso apenas um ConfigRate. Se precisar mudar, mude esse aqui."