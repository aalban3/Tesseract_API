from newsapi import NewsApiClient as News
from textblob import TextBlob as tb
from datetime import date, timedelta, datetime
from .news_sentiment import SentimentAnalysis
import json
import os
import time

news_key = os.getenv('NEWS_KEY')

# Init
class NewsApi:
    def __init__(self, topic = None,sdate=(datetime.now() - timedelta(days=1)),edate=date.today(),lang = 'en',src='google-news',cat='',ctry='us'):
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
        top_headlines = self._newsAPI.get_top_headlines(
                                          language=self.lang,
                                          country=self.ctry)
        #q=self.topic,
        return top_headlines
    # /v2/everything
    def get_all_news(self,domain='bbc.co.uk,techcrunch.com',sort_by='relevancy',pg=2):
        all_articles = self._newsAPI.get_everything(q=self.topic,
                                      sources=self.src,
                                      domains=domain,
                                      from_param=self.sdate,
                                      to=self.edate,
                                      language=self.lang,
                                      sort_by=sort_by,
                                      page=pg)    
        return all_articles
    # /v2/sources
    def get_sources(self):
        return self._newsAPI.get_sources()

class ArticleStruct:
    def __init__(self,author,title,description,url,content,source,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.content = content
        self.source = source
        self.publishedAt = publishedAt
class MakeNewsObj:
    def __init__(self,topic=None):
        self.topic = topic
    def headlines_obj(self):
        #start = time.time()
        news_res = NewsApi().get_headlines()
        articles = news_res['articles']
        news_obj = list()
        to_analyze = list()
        for article in articles:
            to_analyze.append(article['content'])
            article_obj = ArticleStruct(
                author          = article['author'],
                title           = article['title'],
                description     = article['description'],
                url             = article['url'],
                content         = article['content'],
                source          = article['source']['name'],
                publishedAt     = article['publishedAt']
            )
            news_obj.append(article_obj)
        seen_phrases = {}
        for content in to_analyze:
            if content != None:
                noun_phrases = SentimentAnalysis(content).get_noun_phrases()
                for phrase in noun_phrases:
                    if phrase in seen_phrases.keys():
                        seen_phrases[phrase] += 1
                    else:
                        seen_phrases[phrase] = 1
        #end = time.time()  
        #print(f'Function took {end - start} seconds')     
        return news_obj
    
    def topic_obj(self):
        news_res = NewsApi(topic=self.topic).get_headlines()
        json_res = json.dumps(news_res)
        news = json.loads(json_res)
        return news
    