import json
# Create your tests here.
def cityToTeam(city):
	teamname = ""
	dat = json.load(open("static\data\mlbteammappings.json"))
	print(dat["team_all"]["copyRight"])
	for team in dat["team_all"]["queryResults"]["row"]:
		if team["city"] == city.capitalize():
			teamname = team["name"]
		
	
	return teamname