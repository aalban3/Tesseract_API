from rest_framework import serializers
from .twitter import TweetStruct

class TweetSerializer(serializers.Serializer):
    user            = serializers.CharField(max_length=20)
    text            = serializers.CharField(max_length=280)
    created_at      = serializers.CharField(max_length=30)
    country         = serializers.CharField(max_length=30)
    country_code    = serializers.CharField(max_length=10)
    tweet_id        = serializers.CharField(max_length=50) # using id_str from response
    
    def create(self, validated_data):
        return TweetStruct(**validated_data)
