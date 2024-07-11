import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    '''Tests class for SentimentAnalysis package'''
    def test_sentiment_analyzer(self):
        '''Tests for sentiment_analyzer function'''
        text = 'I love working with Python'
        response = sentiment_analyzer(text)
        self.assertEqual(response['label'], 'positive') # “I love working with Python”: “SENT_POSITIVE”
        text = 'I hate working with Pyhton'
        response = sentiment_analyzer(text)
        self.assertEqual(response['label'], 'negative')  # “I hate working with Pyhton”: “SENT_NEGATIVE”
        text = 'I am neutral on Python'
        response = sentiment_analyzer(text)
        self.assertEqual(response['label'], 'neutral')  # “I am neutral on Python”: “SENT_NEUTRAL”

unittest.main()
