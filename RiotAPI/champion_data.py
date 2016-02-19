from cassiopeia import riotapi

def riotapi_setup():
	riotapi.set_region("NA")
	riotapi.set_api_key("aa751b44-85aa-447b-ad09-6b004dcf0e8c")

def get_summoner():
	summonerName = raw_input("Summoner name: ")
	return riotapi.get_summoner_by_name(summonerName)

def get_champion_stats( summoner ):
	return riotapi.get_ranked_stats(summoner)

def ranked_win_percent( championStats ):
	winPercentList = []
	for champion in championStats:
		winPercentList.append((champion, championStats[champion]))
	winPercentList.sort(compare_champion_win_percent)
	print "Win percentages by champion in ranked: "
	for championTuple in winPercentList:
		print "%s : %f" % (championTuple[0], (((championTuple[1].wins * 1.0) / championTuple[1].games_played) * 100))

def compare_champion_win_percent( champ1, champ2 ):
	winP1 = (((champ1[1].wins * 1.0) / champ1[1].games_played) * 100)
	winP2 = (((champ2[1].wins * 1.0) / champ2[1].games_played) * 100)
	#return winP1 - winP2
	if winP1 > winP2:
		return -1
	elif winP1 < winP2:
		return 1
	else:
		return 0

#setup riotapi
riotapi_setup()
summoner = get_summoner()
championStats = get_champion_stats( summoner )
ranked_win_percent( championStats )