from django.urls import path, re_path
from .views import tweet_list

urlpatterns = [
    path('tweets/', tweet_list), # list and create
    path('tweets/<query_value>/', tweet_list)
]