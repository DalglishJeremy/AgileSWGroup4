from django.db import models
from django.conf import settings

class MlbBoxScoreData(models.Model):
	boxscore = models.TextField()
	away_name = models.TextField()
	away_abbr = models.TextField(max_length = 5)
	away_score = models.IntegerField()
	home_name = models.TextField()
	home_abbr = models.TextField(max_length = 5)
	home_score = models.IntegerField()
	winning_name = models.TextField()
	winning_abbr = models.TextField(max_length = 5)
	losing_name = models.TextField()
	losing_abbr = models.TextField(max_length = 5)

# Create your models here.
