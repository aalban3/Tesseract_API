Project Overview
----------------
I'm building an interactive application that combines Twitter data and stock market data to provide users with investing insights. I'm using Django to build my back-end and eventually I will add a new repository for the Machine Learning portion of the project.

Django Apps
-----------
Search:
*  This Application takes input from a text form 
*  The input triggers the Tweepy API and returns 5 of the latest tweets that mention the search query item
*  The App redirects to the search-results page that shows the retuned tweets
tweets:
*  Taking the output from the Search App, I'm using this to extract specific data about the tweet
*  I'm uploading the tweets to a DynamoDB instance in AWS 
*  This App will also generate a table with the following fields
               |TweetDate| User| InReplyTo|Sentiment
*  The Sentiment field is still a work in progress. I have a Textblob sentiment algorithm, but I might take it a little further with TensorFLow
Price Chart:
*  I'm going to use Alphavantage API to pull stock data
*  NumPy will be used to structure my data and I will display a chart using Matplotlib or something similar.

News:
* Search news articles based on stock tickers or market topics
* News are displayed in chronological order
* User will have the option to view top articles or everything related to a topic 
