import re
from string import punctuation 
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer

class PreProcessTweets: 
	def __init__(self):
		stopword = stopwords.words('english')
		self._stopwords = set(stopword)
		self._lemmatizer = WordNetLemmatizer()
		

	def processTweets(self, tweets):
		processed_tweets = []
		for tweet in tweets:
			processed_tweets.append(self._processTweet(tweet["text"]))
		return processed_tweets

	def _processTweet(self, tweet):

		tweet = tweet.lower() # convert to lower-case
		tweet = re.sub(r'http\S+', '', tweet) # remove URLs
		tweet = re.sub(r"\\[a-z][a-z]?[0-9]+", '', tweet)
		tweet = re.sub('[^A-Za-z ]+', '', tweet) # only allow letters
		tweet = tweet.split(" ") # tokenize tweets
		tweet = [word for word in tweet if len(word) > 2] # remove words with < 2 characters
		tweet = [self._lemmatizer.lemmatize(word) for word in tweet] # lemmatize tweets

		return [word for word in tweet if word not in self._stopwords]

	def lemmatizeWords(self, tweet):
		lemmatizer = WordNetLemmatizer()
		return [lemmatizer.lemmatize(word) for word in tweet]
