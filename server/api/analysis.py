from textblob import TextBlob
import numpy as np
import nltk
from collections import defaultdict, Counter
from joblib import load

nltk.download("vader_lexicon")

pipeline = load("../ml_model/tweet_classification.joblib")

from nltk.sentiment.vader import SentimentIntensityAnalyzer


class SentimentAnalyser:
    def scoreTweets(self, tweets):

        score_count = defaultdict(int)

        scores = [
            SentimentIntensityAnalyzer().polarity_scores(tweet["text"])
            for tweet in tweets
        ]

        for score in scores:
            if score["compound"] > 0.0:
                score_count["pos"] += 1
            elif score["compound"] < 0.0:
                score_count["neg"] += 1
            else:
                score_count["neu"] += 1

        return score_count

    def getSentiment(self, tweets):

        scores = pipeline.predict([tweet["text"] for tweet in tweets])
        print("SCORES", scores)
        return Counter(scores)
