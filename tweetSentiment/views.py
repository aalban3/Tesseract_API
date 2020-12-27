from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from .serializers import TweetSerializer
import json
from .twitter import ApiAuth, MakeObj, TweetStruct

def tweet_list(request, query_value):
    if request.method == 'GET':
        tweet_obj = MakeObj(query_value).get_object()
        serializer = TweetSerializer(tweet_obj)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TweetSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return  JsonResponse(serializer.errors,  status=400)