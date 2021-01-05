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
        serializer_objects = list()
        # serializer only takes one object at a time
        # loop through the object and get the data from it before returning
        for obj in tweet_obj:
            serializer_objects.append(TweetSerializer(obj).data)
        
        return JsonResponse(serializer_objects, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TweetSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return  JsonResponse(serializer.errors,  status=400)