# Tesseract API - Stock Market Sentiment Analysis 
Welcome to the Tesseract API page! this project reflects my fascination with AI and Financial data. I believe there are lots of insights that can be extracted from social media and this is my take on Stock Market sentiment analysis. This repository contains the back-end API I designed for my React front-end to consume. I chose Django Rest Framework because of its vast variety of AI/ML libraries. At this stage in the develppment cycle I am only using the Twitter API ([Tweepy](http://github.com)) and [TextBlob](https://textblob.readthedocs.io/en/dev/) for [Natural Language Processing](https://becominghuman.ai/a-simple-introduction-to-natural-language-processing-ea66a1747b32)
### Search
* The Tesseract front-end app sends a request and gets back 
* The search is going to be optimized for Stock searches, but it can retrieve any tweets it can find that match the search 
### Tweets
* This App will return a serialized object with the following fields
    * user
    * tweet body
    * creation date
    * country code
    * country
    * tweet id
*  The Sentiment field is still a work in progress. I have a Textblob sentiment algorithm, but I might take it a little further with TensorFLow

### News
* Search news articles based on stock tickers or market topics
* Initial version will display top 5 articles as well as the Sentiment analysis for each article
* News are displayed in chronological order and can be filtered 
    * I have plans of improving search wwith GraphQL in a future release
* User will have the option to view top articles or everything related to a topic 
