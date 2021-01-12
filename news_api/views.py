from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
import json
from .src import NewsApi

# Create your views here.

def tickerNews(request, topic):
    if request.method == 'GET':
        news_obj = MakeObj(query_value).get_object()
        serializer_objects = list()
        for obj in tweet_obj:
            serializer_objects.append(TweetSerializer(obj).data)
        return JsonResponse(serializer_objects, safe=False)
 
def allNews(request):
    if request.method == 'GET':
        my_news = NewsApi(topic='parler')
        top_headlines = my_news.get_headlines()
        return JsonResponse(top_headlines, safe=False)