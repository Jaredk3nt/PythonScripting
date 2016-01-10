import sys

EARTH_ORBIT = 584000000.0
C = 186282.0

def findAge(age):
	distance = age * EARTH_ORBIT
	l_time = ((distance / C) / 60.0) / 60.0 #how many seconds it took light to travel how far you've gone
	return l_time


print "How old are you?"
age = input()
l_age = findAge(age)
print "You are approximately %f light hours old" % l_age
