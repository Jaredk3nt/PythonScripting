import praw 
import pdb
import re
import os
from configBot import *
from PIL import Image
from urllib2 import Request, urlopen
from StringIO import StringIO
from datetime import datetime
#necessary methods
imageTypes = ['png', 'jpg', 'jpeg']

#necessary naming and logins
user_agent = ("WallpaperGrabber v 0.1")
r = praw.Reddit(user_agent = user_agent)
r.login(REDDIT_USERNAME, REDDIT_PASS)

#choose subreddit to pull top photos from
#subreddits = [r.get_subreddit("wallpapers"), r.get_subreddit("wallpaper")]
subreddit = r.get_subreddit("wallpapers")

#creating directory for the date and creating path
path = ['/home/jared/Pictures/Wallpapers/']
date = datetime.now().strftime("%y-%d-%m/")
path.append(date)
newPath = ''.join(path)
#if the dir for the current date does not exist creat it
if not os.path.exists(newPath):
	os.makedirs(newPath)
	print "Directory created at : ", newPath
#create a list of files to make sure you are not duplicating any images
files = os.listdir(newPath)

#loop over the top posts in wallpapers
for submission in subreddit.get_hot(limit = 20):
	#if they post contains a photo
	if submission.url.split('.')[-1] in imageTypes\
		or 'imgur' in submission.domain.split('.'):
			rq = Request(submission.url)
        		response = urlopen(rq)
    			data = response.read()        
    			try:
        			im = Image.open(StringIO(data))
        			im.verify()
        			#reset list to path
        			fpath = [newPath]
        			#get name and type from url
        			fname = submission.url.split('/')[-1]
        			fpath.append(fname)

        			finalPath = ''.join(fpath)
        			#check for duplicates
        			new = True
        			if files:
        				for name in files:
        					if (fname == name):
        						new = False
        						break
        			
        			if new:
        				Image.open(StringIO(data)).save(finalPath)
        				print "Saved: ", finalPath

    			except:
        			continue
	else:
		continue


