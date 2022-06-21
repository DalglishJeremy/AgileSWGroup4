from django.db import models
from django.conf import settings

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #show the actual city name on the dashboard
        return self.name
    
    class Meta: 
        verbose_name_plural = 'cities'

class MlbBoxScoreData(models.Model):
	game_number = models.IntegerField()
	date_played = models.TextField()
	boxscore = models.TextField()
	away_name = models.TextField()
	away_abbr = models.TextField(max_length = 5)
	away_score = models.IntegerField()
	away_logo_path = models.TextField()
	home_name = models.TextField()
	home_abbr = models.TextField(max_length = 5)
	home_score = models.IntegerField()
	home_logo_path = models.TextField()
	winning_name = models.TextField()
	winning_abbr = models.TextField(max_length = 5)
	losing_name = models.TextField()
	losing_abbr = models.TextField(max_length = 5)

class NbaBoxScoreData(models.Model):
	game_number = models.IntegerField()
	date_played = models.TextField()
	boxscore = models.TextField()
	away_name = models.TextField()
	away_abbr = models.TextField(max_length = 5)
	away_score = models.IntegerField()
	away_logo_path = models.TextField()
	home_name = models.TextField()
	home_abbr = models.TextField(max_length = 5)
	home_score = models.IntegerField()
	home_logo_path = models.TextField()
	winning_name = models.TextField()
	winning_abbr = models.TextField(max_length = 5)
	losing_name = models.TextField()
	losing_abbr = models.TextField(max_length = 5)
# Create your models here.
