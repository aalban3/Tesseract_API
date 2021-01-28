from rest_framework import serializers
from .src import ArticleStruct

class ArticleSerializer(serializers.Serializer):
    author              = serializers.CharField(max_length=20)
    title               = serializers.CharField(max_length=150)
    description         = serializers.CharField(max_length=120)
    url                 = serializers.URLField(max_length=200, min_length=None, allow_blank=True)
    content             = serializers.CharField(max_length=280)
    source              = serializers.CharField(max_length=50)
    publishedAt         = serializers.CharField(max_length=30)
    
    def create(self, validated_data):
        return ArticleStruct(**validated_data)