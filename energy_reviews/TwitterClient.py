import json
import urllib2
from QueryBuilder import QueryBuilder
from pyquery import PyQuery
from Tweet import Tweet
import datetime

"""
Represents a client that connects to Twitter to retrieve tweets based on a
search criteria.

Initially this class was going to use the Twitter REST API and Tweepy, but that
would only retrieve tweets from the last week.

There is a workaround to retrieve older tweets by sending an HTTP GET request
and replicating the browser's behaviour when scrolling down and loading older
tweets using the min_position and max_position arguments.

"""

class TwitterClient:
    def __init__(self):
        pass

    def get_tweets(self, twitterQuery):
        """
        Sends query to Twitter and mimics behaviour of browser scrolling down
        using min_position and max_position params.

        Args:
            twitterQuery: query object containing search parameters.

        Returns:
            json: total query results in JSON format.
        """
        min_position = ''

        tweets = []

        #Reload Twitter page results until we reach number of desired tweets
        while len(tweets) < twitterQuery.count:
            print "len(tweets) = " + str(len(tweets))
            print "twitterQuery.count = " + str(twitterQuery.count)
            response = self._send_request(twitterQuery)
            tweets.extend(self._parse_tweets(response))

            if len(self._parse_tweets(response)) == 0:
                return tweets
            else:
                #Update Twitter Query with min/max positions
                min_position = response['min_position']
                twitterQuery.update(max_position=min_position)

        return tweets

    def _send_request(self, twitterQuery):
        """
        Elaborates and sends Twitter HTTP GET request.

        Args:
            twitterQuery: query object containing search parameters.

        Returns:
            json: partial query results containing matching tweets in json
                format, from min_position to max_position
        """
        builder = QueryBuilder(twitterQuery)
        url = builder.get_url()

        headers = \
            {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)'}

        request = urllib2.Request(url, headers = headers)

        response = urllib2.urlopen(request).read()

        response_json = json.loads(response)

        return response_json

    def _parse_tweets(self, response):
        """
        Twitter's response is a json object containing an html page where the
        tweets are listed.
        """
        tweets = []
        print response
        if response['items_html'] != u'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n':
            tweet_html_list = PyQuery(response['items_html'])('div.js-stream-tweet')

            for tweet_html in tweet_html_list:
                pq = PyQuery(tweet_html)
                tweet = Tweet()
                tweet.username = pq('span.username.js-action-profile-name b').text()
                tweet.message = pq('p.js-tweet-text').text()
                tweet.created_at = datetime.datetime.fromtimestamp(int(pq('small.time span.js-short-timestamp').attr('data-time')))
                tweet.id = pq.attr('data-tweet-id')
                tweet.permalink = 'https://twitter.com' + pq.attr('data-permalink-path')
                tweet.location = pq('span.Tweet-geo')
                tweets.append(tweet)
                tweet.pretty_print()

        return tweets


    #def _pretty_print(tweet):
    #    """
    #    Prints each non-private element of the tweet for debug.
    #    """
    #    for param in dir(tweet):
    #        if not param.startswith('_'):
    #            print "%s : %s\n" % (param, eval('tweet.' + param))
