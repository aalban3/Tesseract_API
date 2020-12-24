import json
import tweepy
from tweepy import OAuthHandler
from tweepy.parsers import JSONParser
from os import environ

consumer_key            = environ.get('CONSUMER_KEY')
consumer_secret         = environ.get('CONSUMER_SECRET')
access_token            = environ.get('ACCESS_TOKEN')
access_token_secret     = environ.get('ACCESS_TOKEN_SECRET')
class ApiAuth:
    def __init__(self,ticker):
        self.ticker = ticker

    def auth(self):
        consumer_creds = dict();
        consumer_creds['consumer'] = consumer_key
        consumer_creds['consumer_secret'] = consumer_secret
        consumer_creds['access_token'] = access_token
        consumer_creds['access_token_secret'] =  access_token_secret

        auth = tweepy.OAuthHandler(consumer_creds['consumer'], consumer_creds['consumer_secret'])
        auth.set_access_token(consumer_creds['access_token'], consumer_creds['access_token_secret'])
        api = tweepy.API(auth)
        return api

    def get_tweets(self): 
        query = self.ticker
        count = 1
        api = self.auth()
        new_tweets = api.search(q=query, count=count, lang="en")
        return new_tweets