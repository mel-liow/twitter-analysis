import re
from string import punctuation 
import nltk
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer

class PreProcessTweets: 
	def __init__(self):
		stopword = stopwords.words('english')
		self._stopwords = set(stopword + list(punctuation) +['AT_USER','URL'] )

	def processTweets(self, tweets):
		processed_tweets = []
		for tweet in tweets:
			processed_tweets.append(self._processTweet(tweet["text"]))
		return processed_tweets

	def _processTweet(self, tweet):
		tweet = tweet.lower() # convert to lower-case
		tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet) # remove URLs
		tweet = re.sub('@[^\s]+', 'AT_USER', tweet) # remove usernames
		tweet = re.sub(r'#([^\s]+)', r'\1', tweet) # remove the # in #hashtag
		tweet = tweet.split(" ") # tokenize tweets
		return [word for word in tweet if word not in self._stopwords]

	def lemmatizeWords(self, tweet):
		lemmatizer = WordNetLemmatizer()
		return [lemmatizer.lemmatize(word) for word in tweet]
