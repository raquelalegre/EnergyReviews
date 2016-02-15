"""
Represents a client that connects to Twitter to retrieve tweets based on a
search criteria using Twitter REST API and Tweepy.
"""
import tweepy
import json
from tweepy import OAuthHandler

class TwitterClient:
    def __init__(self):
        self.api = self._get_twitter_api()

    def _get_twitter_api(self):
        """
        Since we are only reading public information from Twitter, we don't need
        access token/secret values.
        """
        with open('secrets.json') as secrets_file:
            secrets = json.load(secrets_file)

        consumer_key = secrets['consumer_key']
        consumer_secret = secrets['consumer_secret']

        auth = OAuthHandler(consumer_key, consumer_secret)

        return tweepy.API(auth)
