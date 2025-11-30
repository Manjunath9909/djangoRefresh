from django.db import models

# Create your models here.
class leaderboard(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    time = models.FloatField()

