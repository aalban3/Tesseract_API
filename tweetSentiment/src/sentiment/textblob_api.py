from textblob import TextBlob
import sys
from os import environ
sys.path.append(environ.get('SENTIMENT_PATH'))
from twitter import ApiAuth

class SentimentAnalysis:
    def __init__(self, data):
        self.data = TextBlob(data)
    def get_tags(self):
        return  self.data.tags
        
