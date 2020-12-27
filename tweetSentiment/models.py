from django.db import models
from django.core.validators import RegexValidator
ALPHANUMERIC = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
# Create your models here.
class Tweet(models.Model):
    body            = models.CharField(max_length= 280)
    user            = models.CharField(max_length= 50)
    tweet_id        = models.CharField(max_length=50, blank=False, null=False, validators=[ALPHANUMERIC])
    creation_date   = models.DateField()
    country_code    = models.CharField(max_length=2)
    country         = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user
    
    def update_tweets(self,tweets):
        tweetObj = ApiAuth('$TSLA')
        raw_tweets = tweetObj.get_tweets()
        json_tweets = json.dumps(raw_tweets[2]._json)
        tweets = json.loads(json_tweets)
        #print(json.dumps(tweets, indent=4, sort_keys=True))
        #tweet_inst = tweets[0]

        print("screen name: " + tweets["user"]["screen_name"])
        print("crrated: " + tweets["created_at"])
        print("tweet body: " + tweets["text"])

        if tweets["place"] is not None:
            country = tweets["place"]["country"]
            print("country: " + country)
        else:
            print("country: None")

        if tweets["place"] is not None:
            country_code = tweets["place"]["country_code"]
            print("country code: " + country_code)
        else:
            print("country code: None")