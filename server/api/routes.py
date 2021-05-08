import time
import numpy as np
import matplotlib.pyplot as plt
import re
from twython import Twython
from flask import request
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('wordnet')

wn = nltk.WordNetLemmatizer()
stopword = nltk.corpus.stopwords.words('english')

from api import app

twitter = Twython(app.config["TWITTER_KEY"], app.config["TWITTER_SECRET"])

@app.route('/twitter', methods=['POST'])
def get_data():
	data = request.json
	twitterHandle = data['twitterHandle']

	#Get timeline 
	user_timeline=twitter.get_user_timeline(screen_name=twitterHandle,count=1) 
	last_id = user_timeline[0]['id']-1
	batch = twitter.get_user_timeline(screen_name=twitterHandle,count=200, max_id=last_id)
	user_timeline.extend(batch)

	#Extract textfields from tweets
	raw_tweets = []
	for tweets in user_timeline:
		raw_tweets.append(tweets['text'])

	
	#Clean up words
	words_no_punct = remove_punct(raw_tweets)
	words_tokenized = tokenization(words_no_punct)
	words_no_stopwords = remove_stopwords(words_tokenized)
	words_lemmatized = lemmatizer(words_stemmed)

	return { 'words': words_lemmatized }


def remove_punct(text):
	text = ''.join(text)
	text = re.sub(r'http\S+', '', text)
	text = re.sub(r"\\[a-z][a-z]?[0-9]+", '', text)
	text = re.sub('[^A-Za-z ]+', '', text)
	return text

def tokenization(text):
	text = text.split(" ")
	return text

def remove_stopwords(text):
	text = [w for w in text if len(w) > 2]
	text = [w.lower() for w in text]
	text = [word for word in text if word not in stopword]
	return text

def lemmatizer(text):
  text = [wn.lemmatize(word) for word in text]
  return text
