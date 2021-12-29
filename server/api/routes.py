from flask import request
from .preprocess import PreProcessTweets
from .analysis import SentimentAnalyser
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
	tweets = twitter.get_user_timeline(screen_name=twitter_handle, count=1) 
	last_id = tweets[0]['id']-1
	batch = twitter.get_user_timeline(screen_name=twitter_handle, count=200, max_id=last_id)
	tweets.extend(batch)
	
	tweet_processor = PreProcessTweets()

	processed_tweets = tweet_processor.processTweets(tweets)
	words = [word for tweet in processed_tweets for word in tweet]

	fdist = FreqDist(words)
	frequent_words = json.dumps(fdist.most_common(50))


	# for sentiment analysis
	sentiment_tweets = twitter.search(q=twitter_handle + '-filter:retweets AND -filter:replies', count=100)
	tweet_analyser = SentimentAnalyser()
	scores = tweet_analyser.scoreTweets(sentiment_tweets['statuses'])
	print(f'SCORED TWEETS', scores)


	return { 'words': frequent_words, 'scores': scores}


@app.route('/sentiment', methods=['POST'])
def get_sentiment():
	data = request.json
	search_term = data['twitterHandle']

	#Get tweets - fetches max 100 tweets
	tweets = twitter.search(q=search_term + '-filter:retweets AND -filter:replies', count=100)

	tweet_analyser = SentimentAnalyser()
	scored_tweets = tweet_analyser.scoreTweets(tweets['statuses'])
	print(f'SCORED TWEETS', scored_tweets)

	return [scored_tweets]