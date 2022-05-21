from datetime import datetime, timedelta
from sportsipy.mlb.boxscore import Boxscores
import json

today = datetime.today()
yesterday = datetime.today() - timedelta(1)

games = Boxscores(yesterday)

#gamesToday = games.games.get(yesterday);

yesterdayString = yesterday.strftime("%#m-%#d-%Y").split(" ")[0]

gamesDictionaryList = []
gamesDictionary = {}
gameCounter = 1;

for game in games.games[yesterdayString]:
	gamesDictionary["model"] = "Sports.MlbBoxScoreData"
	gamesDictionary["pk"] = gameCounter
	gamesDictionary["fields"] = game
	gamesDictionaryList.append(gamesDictionary.copy())
	gamesDictionary.clear()
	gameCounter += 1

out = json.dumps(gamesDictionaryList, indent = 1)

outfile = open("fixtures/mlbfixture", "w")
outfile.write(out)
outfile.close()

print(out)

