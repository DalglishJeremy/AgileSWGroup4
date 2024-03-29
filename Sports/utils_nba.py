from datetime import datetime, timedelta
from sportsipy.nba.boxscore import Boxscores
import json
from .models import *

def populateBoxScoresDefaultNBA():
	today = datetime.today()
	yesterday = datetime.today() - timedelta(1)

	games = Boxscores(yesterday)
	print(yesterday)

	yesterdayString = yesterday.strftime("%#m-%#d-%Y").split(" ")[0]

	gameCounter = 1;

	if not NbaBoxScoreData.objects.filter(date_played=yesterdayString).exists():
		for game in games.games[yesterdayString]:
			NbaBoxScoreData.objects.create(
				game_number = gameCounter,
				date_played = yesterdayString,
				boxscore = game["boxscore"],
				away_name = game["away_name"],
				away_abbr = game["away_abbr"],
				away_score = game["away_score"],
				away_logo_path = "BaseballLogos/" + game["away_abbr"] + ".png",
				home_name = game["home_name"],
				home_abbr = game["home_abbr"],
				home_score = game["home_score"], 
				home_logo_path = "BaseballLogos/" + game["home_abbr"] + ".png",
				winning_name = game["winning_name"],
				winning_abbr = game["winning_abbr"],
				losing_name = game["losing_name"],
				losing_abbr = game["losing_abbr"])
			gameCounter += 1

	return yesterdayString


def populateNBABoxScores(date):
	# format
	format = '%Y-%m-%d'

	# convert from string format to datetime format
	dt = datetime.strptime(date, format)

	games = Boxscores(dt)
	print(dt)

	dateString = dt.strftime("%#m-%#d-%Y").split(" ")[0]

	gameCounter = 1;

	if not NbaBoxScoreData.objects.filter(date_played=dateString).exists():
		for game in games.games[dateString]:
			NbaBoxScoreData.objects.create(
				game_number = gameCounter,
				date_played = dateString,
				boxscore = game["boxscore"],
				away_name = game["away_name"],
				away_abbr = game["away_abbr"],
				away_score = game["away_score"],
				away_logo_path = "BasketballLogos/" + game["away_abbr"] + ".png",
				home_name = game["home_name"],
				home_abbr = game["home_abbr"],
				home_score = game["home_score"], 
				home_logo_path = "BasketballLogos/" + game["home_abbr"] + ".png",
				winning_name = game["winning_name"],
				winning_abbr = game["winning_abbr"],
				losing_name = game["losing_name"],
				losing_abbr = game["losing_abbr"])
			gameCounter += 1

	return dateString


