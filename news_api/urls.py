from django.urls import path, re_path
from .views import tickerNews, allNews

urlpatterns = [
    path('headlines/', allNews), # list and create
    path('news/<topic>/', tickerNews)
]