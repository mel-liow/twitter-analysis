import time
import numpy as np
import matplotlib.pyplot as plt
import re
from twython import Twython
from flask import request

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
stopwords.words('english')

from api import app

twitter = Twython(app.config["TWITTER_KEY"], app.config["TWITTER_SECRET"])

@app.route('/twitter', methods=['POST'])
def get_data():
	data = request.json
	twitterHandle = data['twitterHandle']
	#Get timeline 
	user_timeline=twitter.get_user_timeline(screen_name=twitterHandle,count=1) 

	#get most recent id
	last_id = user_timeline[0]['id']-1
	batch = twitter.get_user_timeline(screen_name=twitterHandle,count=200, max_id=last_id)
	user_timeline.extend(batch)
	last_id = user_timeline[-1]['id'] - 1

	#Extract textfields from tweets
	raw_tweets = []
	for tweets in user_timeline:
		raw_tweets.append(tweets['text'])


	raw_string = ''.join(raw_tweets)

	no_links = re.sub(r'http\S+', '', raw_string)
	no_unicode = re.sub(r"\\[a-z][a-z]?[0-9]+", '', no_links)
	no_special_characters = re.sub('[^A-Za-z ]+', '', no_unicode)

	stop_words = set(stopwords.words('english'))

	words = no_special_characters.split(" ")
	words = [w for w in words if len(w) > 2]
	words = [w.lower() for w in words]
	words = [w for w in words if w not in stop_words]

	return { 'words': words }