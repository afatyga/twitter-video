#EC500 HW 3
#Alex Fatyga

import keys #holds the keys for using tweepy
import tweepy #twitter api
import ffmpy #for hw3

from PIL import Image, ImageDraw #to save the text as an image

import io
import os
import urllib.request as req #to convert the url into an image file
import json #to output a json file for the user

from datetime import datetime
# datetime object containing current date and time

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d")

def saveAsFile(filename, textOrFile, boolTextOrFile):
	if (boolTextOrFile == 0):
		img = Image.new('RGB', (1000, 200), color = (73, 109, 137))
 
		d = ImageDraw.Draw(img)
		d.text((10,10), textOrFile, fill=(255,255,0))
 
		img.save(filename)

	elif (boolTextOrFile == 1):
		req.urlretrieve(textOrFile, filename)


#first function, takes in a string of the twitter username, creates a json file of the output and returns a 1 or 0 to indicate success or failure
def getMsgs(username):

	if not isinstance(username,str): #can only take in a string
		return 0
	auth = tweepy.OAuthHandler(keys.key, keys.secretKey) #using key from keys file - blank in github
	auth.set_access_token(keys.accessToken, keys.accessTokenSecret)
	tweets = ""
	api = tweepy.API(auth)

	#use the following 2 lines for writing to json
	data = {}
	data['tweets'] = []
	countTweets = 0 

	try:	#will be an error if the username is valid
		for status in tweepy.Cursor(api.user_timeline,username).items(20): #gets past 20 tweets
			    
			tweetDateTime = str(status.created_at)
			dateTime = tweetDateTime.split()

			if (dateTime[0] == dt_string): #will only get tweets from the past day

				tweets = tweets + "\n" + status.text # will also print tweets and google vision detection to terminal
				countTweets = countTweets + 1
				file_name = "tweet" + str(countTweets) + ".png"

				saveAsFile(file_name, str(status.text), 0)

				try: #will only do the next line if there is an image
					for link in status.entities['media']:
						url = str(link['media_url'])
						countTweets = countTweets + 1
						file_name = "image_name" + str(countTweets) + ".jpg"
						saveAsFile(file_name, url, 1)

				except (NameError, KeyError): #if there's no image, append just the text and etc
					pass

		print(tweets)
		return 1 # a success
	except (tweepy.TweepError):
		return 0 #means the username was not valid!

getMsgs("johnmulaneybot")