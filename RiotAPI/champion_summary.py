from cassiopeia import riotapi
from key import API_key

def riotapi_setup():
	riotapi.set_region("NA")
	api_key = API_key()
	riotapi.set_api_key(api_key)

def champion_stats( summoner ):
	statDict = riotapi.get_ranked_stats(summoner, season = None)
	return statDict

def champion_details( champStats ):
	championName = raw_input("Champion: ").title()
	champion = riotapi.get_champion_by_name(championName)
	if champion in champStats:
		champDetails = champStats[champion]
	else:
		print "Champion data not avaliable. Sorry."
		return None
	calculate_ability( champDetails, champion )

def calculate_ability( champStats, champion ):
	#print champStats.to_json()
	assists = champStats.assists
	kills = champStats.kills
	deaths = champStats.deaths
	kda = champStats.kda
	wins = champStats.wins
	losses = champStats.losses
	totalGames = champStats.games_played
	print_stats( assists, kills, deaths, kda, wins, losses, totalGames, champion)

def print_stats( assists, kills, deaths, kda, wins, losses, totalGames, champion):
	print champion
	print "Kills: %d" % kills
	print "Assists: %d" % assists
	print "Deaths: %d" % deaths
	print "KDA: %f" % kda
	print "Total games: %d" % totalGames
	print "Wins: %d" % wins
	print "Losses: %d" % losses
	winPercent = ((wins * 1.0) / totalGames) * 100
	print "Win percentage: %f" % winPercent

def champs_list( champStats ):
	for champion in champStats:
		print "%s : %f" % (champion, (((champStats[champion].wins * 1.0) / champStats[champion].games_played) * 100))

#setup riotapi
riotapi_setup()
summonerName = raw_input("Summoner name: ")
summoner = riotapi.get_summoner_by_name(summonerName)
champStats = champion_stats(summoner)
#calculate_ability( champStats, champion )
champs_list( champStats )
