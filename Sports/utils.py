from datetime import datetime, timedelta
from sportsipy.mlb.boxscore import Boxscores

from .models import *

def populateBoxScores():
	today = datetime.today()
	yesterday = datetime.today() - timedelta(1)

	games = Boxscores(yesterday)

	yesterdayString = yesterday.strftime("%#m-%#d-%Y").split(" ")[0]

	gameCounter = 1;

	for game in games.games[yesterdayString]:
		MlbBoxScoreData.objects.create(
			game_number = gameCounter,
			boxscore = game["boxscore"],
			away_name = game["away_name"],
			away_abbr = game["away_abbr"],
			away_score = game["away_score"],
			home_name = game["home_name"],
			home_abbr = game["home_abbr"],
			home_score = game["home_score"], 
			winning_name = game["winning_name"],
			winning_abbr = game["winning_abbr"],
			losing_name = game["losing_name"],
			losing_abbr = game["losing_abbr"])
		gameCounter += 1