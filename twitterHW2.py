#EC500 HW 3
#Alex Fatyga
import keys #holds the keys for using tweepy
import tweepy #twitter api
from threading import Thread #threading stuff

import os #to get pid id

import subprocess #to run subprocess

from PIL import Image, ImageDraw, ImageFont #to save the text as an image

import urllib.request as req #to convert the url into an image file

from datetime import datetime
# datetime object containing current date and time

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d")
max_tweets = 20
countImages = 0

def createVideo(num): #creates a video of all the images
	videoName = "tweetVid" + str(num) + ".avi"
	startVal = num * 100
	subprocess.run(["ffmpeg","-framerate", "0.33", "-loglevel", "quiet", "-start_number", str(startVal), "-i", "tweets%d.png",videoName])

def imageThreads(listOfLinks, count):
	threads = []
	for (textOrUrl,boolVal) in listOfLinks:
		threads.append(Thread(target = saveAsFile, args = (textOrUrl, boolVal,count)))
		count = count + 1
	return threads

def saveAsFile(textOrUrl, boolVal, count): #goes through the list of tuples and saves images as files
	global countImages	
	filename = "tweets" + str(count) + ".png"
#	countImages = countImages + 1
	if (boolVal == 0):
		img = Image.new('RGB', (1000, 500), color = (73, 109, 137))
		d = ImageDraw.Draw(img)
		font = ImageFont.truetype('arial.ttf', size=14)
		d.text((10,10), textOrUrl, fill=(255,255,0), font = font)
		img.save(filename)
	elif (boolVal == 1):
		req.urlretrieve(textOrUrl, filename)
		image = Image.open(filename)
		new_image = image.resize((400, 400))
		new_image.save(filename)

#first function, takes in a string of the twitter username, creates a json file of the output and returns a 1 or 0 to indicate success or failure
def getMsgs(username):

	if not isinstance(username,str): #can only take in a string
		return []

	auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret) #using key from keys file - blank in github
	auth.set_access_token(keys.access_token, keys.access_secret)

	tweets = ""
	api = tweepy.API(auth)
	listOfLinks = []

	try:	#will be an error if the username is valid
		for status in tweepy.Cursor(api.user_timeline,username).items(max_tweets): #gets past 20 tweets
			    
			tweetDateTime = str(status.created_at)
			dateTime = tweetDateTime.split()

			if (dateTime[0] == dt_string): #will only get tweets from the past day

				tweets = tweets + "\n" + status.text # will also print tweets and google vision detection to terminal
				listOfLinks.append((str(status.text),0))

				try: #will only do the next line if there is an image
					for link in status.entities['media']:
						url = str(link['media_url'])
						listOfLinks.append((str(url), 1))

				except (NameError, KeyError):
					pass

		return listOfLinks # a success
	except (tweepy.TweepError):
		return [] #means the username was not valid!

def startUp(userNum): #my attempt at multi threading
	print("Process with username: " + str(userNum[0]) + " and process id: " + str(os.getpid()) + " is running")

	listOfStuff = getMsgs(userNum[0]) #returns a list of urls/texts to make into images!

	if (listOfStuff == []): return 0 #no images or video to create => either incorrect username or that account just doesn't have any tweets!~

	count = userNum[1] * 100 # when there's multiple processes, you want the images to save as different names
	threads = imageThreads(listOfStuff, count) #creating the threads!
	
	for thread in threads:
		thread.start() #starts the threads

	for thread in threads:
		thread.join() #ends the threads
	
	createVideo(userNum[1])
	print("Video created for user " + userNum[0])
	return 1
