import sys

EARTH_ORBIT = 584000000.0
C = 186282.0

def findAge(age):
	dist = age * EARTH_ORBIT
	print "The Earth  has travelled %d miles while you have been alive" % dist
	l_time = ((dist / C) / 60.0) / 60.0 #how many seconds it took light to travel how far you've gone
	return l_time

def findDist(age):
	age_sec = (((age * 365) * 24) * 60) * 60
	l_dist = age_sec * C
	return l_dist


print "How old are you?"
age = input()
l_age = findAge(age)
l_dist = findDist(age)
print "Based on the Earths movement around the Sun -"
print "You are approximately %f light hours old\n" % l_age
print "Based on traditional measurments of time - "
print "You are approximately %d miles old" % l_dist
