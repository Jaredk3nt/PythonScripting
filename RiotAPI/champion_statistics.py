from cassiopeia import riotapi, type.core.common.Queue
from key import API_key
import MySQLdb

def setup():
	riotapi.set_region("NA")
	api_key = API_key()
	riotapi.set_api_key(api_key)
	return MySQLdb.connect("localhost", "testuser", "test123", "CHAMPIONDB")

def create_table( cur ):
	sql = """ """

def get_matches( summoner, lastDate ):
	queueTypes = [Queue.ranked_solo, Queue.ranked_premade_fives, Queue.ranked_fives, Queue.ranked_dynamic_queue]
	riotapi.get_match_list


db = setup()
cur = con.cursor()
summData = []
sql_date = "SELECT Last_date FROM SUMMONER"
sql_summ = "SELECT summoner_name FROM SUMMONER"
try:
	cur.execute(sql_date)
	lastDate = cur.fetchone()
	cur.execute(sql_summ)
	summoner = cur.fetchone
else:
	print "no last date, pulling all matches."
	lastDate = -1

def get_matches( summoner, lastDate )


db.close()
