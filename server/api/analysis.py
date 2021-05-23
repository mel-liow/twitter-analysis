from textblob import TextBlob
import numpy as np
import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

class SentimentAnalyser: 
	def __init__(self):
		self._positive = 0
		self._neutral = 0
		self._polarity = 0

	def scoreTweets(self, tweets):
		tweet_list = []

		for tweet in tweets:
			tweet_list.append(self._scoreTweet(tweet['text']))
		return tweet_list

	def _scoreTweet(self, tweet):
		analysis = TextBlob(tweet)
		score = SentimentIntensityAnalyzer().polarity_scores(tweet)
		print(score)
		# neg = score[‘neg’]
		# neu = score[‘neu’]
		# pos = score[‘pos’]
		# comp = score[‘compound’]
		# polarity += analysis.sentiment.polarity
		
		# if neg > pos:
		# negative_list.append(tweet.text)
		# negative += 1
		# elif pos > neg:
		# positive_list.append(tweet.text)
		# positive += 1
		
		# elif pos == neg:
		# neutral_list.append(tweet.text)
		# neutral += 1

	def _percentage(numerator, denominator):
		return 100 * float(numerator)/float(denominator)