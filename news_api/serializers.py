from rest_framework import serializers
from .src import ArticleStruct, NewsStruct

class ArticleSerializer(serializers.Serializer):
    author              = serializers.CharField(max_length=20)
    title               = serializers.CharField(max_length=150)
    description         = serializers.CharField(max_length=120)
    url                 = serializers.URLField(max_length=200, min_length=None, allow_blank=False)
    content             = serializers.CharField(max_length=280)
    source              = serializers.CharField(max_length=50)
    publishedAt         = serializers.CharField(max_length=30)
    
    def create(self, validated_data):
        return ArticleStruct(**validated_data)
class NewsSentimentSerializer(serializers.Serializer):
    results             = serializers.IntegerField(max_value=20,min_value=0)
    articles            = ArticleSerializer(many=True) 
    
    def create(self, validated_data):
        return NewsStruct(**validated_data)