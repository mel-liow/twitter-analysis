from flask import request
from .preprocess import PreProcessTweets
from twython import Twython
from nltk import FreqDist
from api import app

import json

twitter = Twython(app.config["TWITTER_KEY"], app.config["TWITTER_SECRET"])


@app.route('/twitter', methods=['POST'])
def get_data():
	data = request.json
	twitter_handle = data['twitterHandle']

	#Get timeline 
	tweets = twitter.get_user_timeline(screen_name=twitter_handle,count=1) 
	last_id = tweets[0]['id']-1
	batch = twitter.get_user_timeline(screen_name=twitter_handle,count=200, max_id=last_id)
	tweets.extend(batch)
	
	tweet_processor = PreProcessTweets()

	processed_tweets = tweet_processor.processTweets(tweets)
	words = [word for tweet in processed_tweets for word in tweet]

	fdist = FreqDist(words)
	frequent_words = json.dumps(fdist.most_common(50))
	return frequent_words

