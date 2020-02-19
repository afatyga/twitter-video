#EC500 HW 3
#Alex Fatyga

import keys #holds the keys for using tweepy
import tweepy #twitter api
from threading import Thread

import subprocess #to run subprocess

from PIL import Image, ImageDraw #to save the text as an image

import urllib.request as req #to convert the url into an image file

from datetime import datetime
# datetime object containing current date and time

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d")

countImages = 0
listOfLinks = []

def createVideo(): #creates a video of all the images
	subprocess.run(["ffmpeg","-framerate", "0.33", "-i", "tweet%d.png", "test.avi"])

def saveAsFile(): #goes through the list of tuples and saves images as files
	global countImages

	for (x, y) in listOfLinks:

		filename = "tweets" + str(countImages) + ".png"

		if (y == 0):
			img = Image.new('RGB', (1000, 200), color = (73, 109, 137))
			d = ImageDraw.Draw(img)
			d.text((10,10), x, fill=(255,255,0))
			img.save(filename)
	
		else:
			req.urlretrieve(x, filename)
	countImages = countImages + 1


#first function, takes in a string of the twitter username, creates a json file of the output and returns a 1 or 0 to indicate success or failure
def getMsgs(username):
	if not isinstance(username,str): #can only take in a string
		return 0
	auth = tweepy.OAuthHandler(keys.key, keys.secretKey) #using key from keys file - blank in github
	auth.set_access_token(keys.accessToken, keys.accessTokenSecret)
	tweets = ""
	api = tweepy.API(auth)

	try:	#will be an error if the username is valid
		for status in tweepy.Cursor(api.user_timeline,username).items(20): #gets past 20 tweets
			    
			tweetDateTime = str(status.created_at)
			dateTime = tweetDateTime.split()

			if (dateTime[0] == dt_string): #will only get tweets from the past day

				tweets = tweets + "\n" + status.text # will also print tweets and google vision detection to terminal
				listOfLinks.append((str(status.text),0))

				try: #will only do the next line if there is an image
					for link in status.entities['media']:
						url = str(link['media_url'])
						listOfLinks.append((str(url)),1)

				except (NameError, KeyError):
					pass
		print("Processed user " + username)
#		print("Tweets: ")
#		print(tweets)
		return 1 # a success
	except (tweepy.TweepError):
		return 0 #means the username was not valid!

def start(username): #my attempt at multi threading
	thread1 = Thread(target = getMsgs, args = (username, ))
	thread2 = Thread(target = saveAsFile)
	thread3 = Thread(target = createVideo)
	thread1.start()
	thread2.start()
	thread3.start()
	thread1.join()
	print("thread 1 finished...exiting")
	thread2.join()
	print("thread 2 finished...exiting")
	thread3.join()
	print("thread 3 finished...exiting")    

start("johnmulaneybot")