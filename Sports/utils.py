from datetime import datetime, timedelta
from sportsipy.mlb.boxscore import Boxscores
import json
from .models import *

def populateBoxScoresDefault():
	today = datetime.today()
	yesterday = datetime.today() - timedelta(1)

	games = Boxscores(yesterday)
	print(yesterday)

	yesterdayString = yesterday.strftime("%#m-%#d-%Y").split(" ")[0]

	gameCounter = 1;

	if not MlbBoxScoreData.objects.filter(date_played=yesterdayString).exists():
		for game in games.games[yesterdayString]:
			MlbBoxScoreData.objects.create(
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

def populateBoxScores(date):
	# format
	format = '%Y-%m-%d'

	# convert from string format to datetime format
	dt = datetime.strptime(date, format)

	games = Boxscores(dt)
	print(dt)

	dateString = dt.strftime("%#m-%#d-%Y").split(" ")[0]

	gameCounter = 1;

	if not MlbBoxScoreData.objects.filter(date_played=dateString).exists():
		for game in games.games[dateString]:
			MlbBoxScoreData.objects.create(
				game_number = gameCounter,
				date_played = dateString,
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

	return dateString

# error with names including spaces
def cityToTeams(city):
	teams = {}
	dat = json.load(open("static\data\mlbteammappings.json"))
	for team in dat["team_all"]["queryResults"]["row"]:
		if team["city"] == city.title():
			teams[team["name"]] = f"BaseballLogos/{team['name_abbrev']}.png"
			#print(f"{team['name']} -> BaseballLogos/{team['name_abbrev']}.png")
	
	return teams
