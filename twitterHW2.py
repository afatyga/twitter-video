#EC500 HW 2
#Alex Fatyga

import keys #holds the keys for using tweepy
import tweepy #twitter api

import io
import os
import urllib.request as req #to convert the url into an image file
import json #to output a json file for the user

# Imports the Google Cloud client library
from google.cloud import vision 
from google.cloud.vision import types

from datetime import datetime
# datetime object containing current date and time

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d")

def getImgDescription(file_name): #takes in the name of the created image file and returns a tuple of the image labels and emotions detected

	client = vision.ImageAnnotatorClient() #using google vision

	#Loads the image into memory
	file_name = os.path.abspath(file_name)
	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()
	image = types.Image(content=content)

    # Performs label detection on the image file
	response = client.label_detection(image=image)
	labels = response.label_annotations
	
	imgDescrip = "The following is detected: "
	length = len(labels)
	count = 0
	
	for label in labels:
	    imgDescrip = imgDescrip + label.description
	    count = count + 1
	    if ( count < (length -1 )):
	    	imgDescrip = imgDescrip + ", "
	    if (count == length - 1):
	    	imgDescrip = imgDescrip + " and "
	imgDescrip = imgDescrip + "."

	image = types.Image(content=content)
	response = client.face_detection(image=image)
	faces = response.face_annotations
	# Names of likelihood from google.cloud.vision.enums

	likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                   		'LIKELY', 'VERY_LIKELY')
	faceDet = ""
	numFace = 0
	for face in faces:
		numFace = numFace + 1
		if (likelihood_name[face.anger_likelihood] == "VERY_LIKELY" or likelihood_name[face.anger_likelihood] == "LIKELY"):
			faceDet = faceDet + " Anger is detected in face " + str(numFace) + "." 
		if (likelihood_name[face.joy_likelihood] == "VERY_LIKELY" or likelihood_name[face.joy_likelihood] == "LIKELY"):
			faceDet = faceDet + " Joy is detected in face " + str(numFace) + "."
		if (likelihood_name[face.surprise_likelihood] == "VERY_LIKELY" or likelihood_name[face.surprise_likelihood] == "LIKELY"):
			faceDet = faceDet + " Surprise is detected in face " + str(numFace) + "."

	return imgDescrip, faceDet

#first function, takes in a string of the twitter username, creates a json file of the output and returns a 1 or 0 to indicate success or failure
def getMsgs(username):

	if not isinstance(username,str): #can only take in a string
		return 0
	auth = tweepy.OAuthHandler(keys.key, keys.secretKey) #using key from keys file - blank in github
	auth.set_access_token(keys.accessToken, keys.accessTokenSecret)
	tweets = ""
	api = tweepy.API(auth)
	num = 0
	#use the following 2 lines for writing to json
	data = {}
	data['tweets'] = []

	try:	#will be an error if the username is valid
		for status in tweepy.Cursor(api.user_timeline,username).items(20): #gets past 20 tweets
			    
			tweetDateTime = str(status.created_at)
			dateTime = tweetDateTime.split()
			if (dateTime[0] == dt_string): #will only get tweets from the past day

				tweets = tweets + "\n" + status.text # will also print tweets and google vision detection to terminal
				try: #will only do the next line if there is an image
					for link in status.entities['media']:
						url = str(link['media_url'])
						num = num +1
						file_name = "image_name" + str(num) + ".jpg"

						req.urlretrieve(url, file_name)
						labels, faceDet = getImgDescription(file_name) #gets labels and face detection info

						tweets = tweets + "\n" + labels + faceDet

						if (faceDet == ""): #if there were no faces detected -> don't add facedet to the json
							data['tweets'].append({ #appending to json
								'user': str(status.user.screen_name),
								'created at': str(status.created_at),
								'text': str(status.text),
								'media': {
									'labels': labels
								}
							})
						else:
							data['tweets'].append({ #appending to json
								'user': str(status.user.screen_name),
								'created at': str(status.created_at),
								'text': str(status.text),
								'media': {
									'labels': labels,
									'emotions detected': faceDet
								}

							})

				except (NameError, KeyError): #if there's no image, append just the text and etc
					data['tweets'].append({
						'user': str(status.user.screen_name),
						'created at': str(status.created_at),
						'text': str(status.text) 
					})

		with open ('tweets.json', 'w') as outfile: #actually adding to the json
			json.dump(data, outfile)
		print(tweets)
		return 1 # a success
	except (tweepy.TweepError):
		return 0 #means the username was not valid!

