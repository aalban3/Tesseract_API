from textblob import TextBlob as tb
from textblob.classifiers import NaiveBayesClassifier
import sys
from os import environ

news = "Senior doctors have asked England's chief medical officer to halve the current 12-week gap between the first and second doses of the Pfizer-Biontech Covid-19 vaccine. The wait was originally three weeks but was then extended, a decision which Prof Chris Whitty said would double the number of people receiving jabs. But, in a letter seen by the BBC, the British Medical Association said the delay was 'difficult to justify'. It comes after the prime minister revealed the UK variant of Covid-19 may be more deadly."

class SentimentAnalysis:
    def __init__(self, data):
        self.data = tb(data)
    def get_tags(self):
        return  self.data.tags
    def get_noun_phrases(self):
        return self.data.noun_phrases
    def get_polarity(self):
        return self.data.sentiment.polarity
    def get_sentiment(self):
        return self.data.sentiment

sentiment = SentimentAnalysis(news)

# print(sentiment.get_tags())
# print(sentiment.get_sentiment())
# print(sentiment.get_sentiment().subjectivity)

ex = tb(news)
print(ex.sentences)
#cl = NaiveBayesClassifier(ex.sentences)