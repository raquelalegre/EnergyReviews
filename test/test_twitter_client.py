import pytest
from unittest import TestCase
from energy_reviews.client import TwitterClient
from energy_reviews.model import Tweet

class TestTwitterClient(TestCase):

    def setup(self):
        """
        Initialize Twitter client.
        """
        self.client = TwitterClient()

    def teardown(self):
        pass

    def test_get_tweet_by_id(self):
        id = 541907082673655808
        text = u'i appear to be crushing on an energy company...  http://t.co/5kE94mrVju go @tempusenergy'
        api = self.client.api
        tweet = api.get_status(id)
        print tweet.text
        assert tweet.text == text
