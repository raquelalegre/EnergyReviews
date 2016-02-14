import json
import urllib2
import QueryBuilder

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
        tweets = {}

        min_position = ''

        #Reload Twitter page results until we reach number of desired tweets
        while len(tweets) < twitterQuery.count:
            response = _send_request(twitterQuery)
            tweets = json.loads(response)

            #Update Twitter Query with min/max positions
            min_position = tweets['min_position']
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

        headers =
            {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)'}

        request = urllib2.Request(url, headers = headers)

        response = urllib2.urlopen(request).read()

        return response

    #def _pretty_print(tweet):
    #    """
    #    Prints each non-private element of the tweet for debug.
    #    """
    #    for param in dir(tweet):
    #        if not param.startswith('_'):
    #            print "%s : %s\n" % (param, eval('tweet.' + param))
