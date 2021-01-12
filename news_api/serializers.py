from rest_framework import serializers
from .src import NewsApi

class TweetSerializer(serializers.Serializer):
    source            = serializers.CharField(max_length=20)
    text            = serializers.CharField(max_length=280)
    created_at      = serializers.CharField(max_length=30)
    country         = serializers.CharField(max_length=30)
    country_code    = serializers.CharField(max_length=10)
    tweet_id        = serializers.CharField(max_length=50) # using id_str from response
    
    def create(self, validated_data):
        return TweetStruct(**validated_data)

    def update(self, instance, validated_data):
         instance.user = validated_data.get('user', instance.user)
         instance.text = validated_data.get('text', instance.text)
         instance.created_at = validated_data.get('created_at', instance.created_at)
         instance.country = validated_data.get('country', instance.country)
         instance.country_code = validated_data.get('country_code', instance.country_code)
         instance.tweet_id = validated_data.get('tweet_id', instance.tweet_id)
         return instance