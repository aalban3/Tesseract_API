from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
import json
from .src import MakeNewsObj
from .serializers import ArticleSerializer

# Create your views here.

def tickerNews(request, topic):
    if request.method == 'GET':
        my_news = MakeNewsObj(topic=topic).headlines_obj()
        return JsonResponse(top_headlines.data, safe=False)
 
def allNews(request):
    if request.method == 'GET':
        my_news = MakeNewsObj().headlines_obj()
        serialized_headlines = list()
        for obj in my_news:
            serialized_headlines.append(ArticleSerializer(obj).data)
        return JsonResponse(serialized_headlines, safe=False) 