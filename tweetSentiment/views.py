from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from .models import Tweet
from .serializers import TweetSerializer
import json 
from django.db import connection

# Create your views here.

def tweet_list(request):
    if request.method == 'GET':
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TweetSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return  JsonResponse(serializer.errors,  status=400)