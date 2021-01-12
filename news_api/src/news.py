from newsapi import NewsApiClient as News
from datetime import date
import json
import os

news_key = os.getenv('NEWS_KEY')

# Init
class NewsApi:
    def __init__(self, topic = None,sdate=date.today(),edate=date.today(), lang = 'en',src='bbc-news',cat='business',ctry='us'):
        self.topic    = topic
        self.sdate    = sdate
        self.edate    = edate
        self.lang     = lang
        self.src      = src 
        self.cat      = cat
        self.ctry     = ctry
        self._newsAPI = News(api_key = news_key)
    def sort_news(self):
        # code to sort news goes in here. Need to learn how to make tables in Django
        pass
    
    # /v2/top-headlines
    def get_headlines(self):
        top_headlines = self._newsAPI.get_top_headlines(q=self.topic,
                                          category=self.cat,
                                          language=self.lang,
                                          country=self.ctry)
        return top_headlines
    # /v2/everything
    def get_all_news(self,domain='bbc.co.uk,techcrunch.com',sort_by='relevancy',pg=2):
        all_articles = self._newsAPI.get_everything(q=self.topic,
                                      #sources=self.src,
                                      domains=domain,
                                      from_param=self.sdate,
                                      to=self.edate,
                                      language=self.lang,
                                      sort_by=sort_by,
                                      page=pg)    
    # /v2/sources
    def get_sources(self):
        return self._newsAPI.get_sources()
    