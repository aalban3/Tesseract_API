import json
import tweepy
from tweepy import OAuthHandler
from tweepy.parsers import JSONParser
import os

consumer_key            = os.getenv('CONSUMER_KEY')
consumer_secret         = os.getenv('CONSUMER_SECRET')
access_token            = os.getenv('ACCESS_TOKEN')
access_token_secret     = os.getenv('ACCESS_TOKEN_SECRET')
class ApiAuth:
    def __init__(self,ticker):
        self.ticker = ticker
    
    def auth(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api

    def get_tweets(self): 
        query = self.ticker
        count = 120
        api = self.auth()
        new_tweets = api.search(q=query, count=count, lang="en")
        return new_tweets

class TweetStruct:
    def __init__(self, user, text, created_at=None, country=None, country_code=None, tweet_id=None):
        self.user = user
        self.text = text
        self.created_at = created_at
        self.country = country
        self.country_code = country_code
        self.tweet_id = tweet_id

class MakeObj:
        def __init__(self,query):
            self.query = query
        
        def get_object(self):
            ### Create Object and pass ticker to get tweets
            tweepy_res = ApiAuth(self.query)
            raw_tweets = tweepy_res.get_tweets()
            tweet_obj = list()
            # loop through all of the tweets you pulled
            # each tweet has to be turned into an object before being returned
            for tweet in raw_tweets:
                json_tweets = json.dumps(tweet._json)
                tweets = json.loads(json_tweets)
                if tweets["place"] is not None:
                    country = tweets["place"]["country"]
                else:
                    country = 'None'
                if tweets["place"] is not None:
                    country_code = tweets["place"]["country_code"]
                else:
                    country_code = 'None'
                temp_obj   =  TweetStruct(
                    user            =   tweets["user"]["screen_name"],
                    text            =   tweets["text"],
                    created_at      =   tweets["created_at"],
                    country         =   country,
                    country_code    =   country_code,
                    tweet_id        =   tweets["id"]
                )
                
                tweet_obj.append(temp_obj)
            
            print(tweet_obj)    
            ## returns multiple objects with all the tweets obtained
            return tweet_obj