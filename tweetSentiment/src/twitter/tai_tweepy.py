import json
import tweepy
from tweepy import OAuthHandler
from tweepy.parsers import JSONParser
import os.path
BASE = os.path.dirname(os.path.abspath(__file__))

class ApiAuth:
    def __init__(self,ticker):
        self.ticker = ticker

    def auth(self):
        with open(os.path.join(BASE, "api_cred.json"),'r') as cred:
            ids = json.load(cred)
        
        consumer_creds = dict();
        consumer_creds['consumer'] = ids['consumer_key']
        consumer_creds['consumer_secret'] = ids['consumer_secret']
        consumer_creds['access_token'] = ids['access_token']
        consumer_creds['access_token_secret'] =  ids['access_token_secret']

        auth = tweepy.OAuthHandler(consumer_creds['consumer'], consumer_creds['consumer_secret'])
        auth.set_access_token(consumer_creds['access_token'], consumer_creds['access_token_secret'])
        api = tweepy.API(auth)
        return api

    def get_tweets(self): 
        query = self.ticker
        count = 20
        api = self.auth()
        new_tweets = api.search(q=query, count=count, lang="en")
        return new_tweets