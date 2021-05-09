from flask import request
import numpy as np
from twython import Twython
import re
import string
import nltk
import json

from nltk import FreqDist
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
  tweets = [tweet['text'] for tweet in user_timeline]
  
  #Clean up words
  words_no_punct = remove_punct(tweets)
  words_tokenized = tokenize(words_no_punct)
  words_no_stopwords = remove_stopwords(words_tokenized)
  words_lemmatized = lemmatize(words_no_stopwords)

  fdist = FreqDist(words_lemmatized)
  frequent_words = json.dumps(fdist.most_common(50))
  return frequent_words


def remove_punct(words):
  words = ''.join(words)
  words = re.sub(r'http\S+', '', words)
  words = re.sub(r"\\[a-z][a-z]?[0-9]+", '', words)
  words = re.sub('[^A-Za-z ]+', '', words)
  return words

def tokenize(words):
  words = words.split(" ")
  return words

def remove_stopwords(words):
  words = [w for w in words if len(w) > 2]
  words = [w.lower() for w in words]
  words = [word for word in words if word not in stopword]
  return words

def lemmatize(words):
  words = [wn.lemmatize(word) for word in words]
  return words
