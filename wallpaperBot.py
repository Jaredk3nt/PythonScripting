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

subreddit = r.get_subreddit("wallpapers")

#creating directory for the date and creating path
path = ['/home/jared/Pictures/Wallpapers/']
date = datetime.now().strftime("%y-%d-%m/")
path.append(date)
newPath = ''.join(path)
if not os.path.exists(newPath):
	os.makedirs(newPath)
print "Directory created at : ", newPath

#loop over the top posts in wallpapers
for submission in subreddit.get_hot(limit = 20)\
	or 'imgur' in submission.domain.split('.'):
	if submission.url.split('.')[-1] in imageTypes:
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
        		#save file under created path
        		Image.open(StringIO(data)).save(''.join(fpath))
        		print "Saved: ", ''.join(fpath)
    		except:
        		continue
	else:
		continue


