from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
import json
from .src import NewsApi, NewsStruct, MakeNewsObj

# Create your views here.

def tickerNews(request, topic):
    if request.method == 'GET':
        my_news = MakeNewsObj(topic=topic)
        
        top_headlines = my_news.headlines_obj()
        return JsonResponse(top_headlines, safe=False)
 
def allNews(request):
    if request.method == 'GET':
        my_news = MakeNewsObj()
        top_headlines = my_news.headlines_obj()
        return JsonResponse(top_headlines, safe=False)