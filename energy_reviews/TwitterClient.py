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

    def get_tweets(twitterQuery):
        """
        Sends query to Twitter and mimics behaviour of browser scrolling down.

        Args:
            twitterQuery: query object containing search parameters.

        Returns:
            json: total query results in JSON format.
        """
        pass

    def send_request(twitterQuery):
        """
        Elaborates and sends Twitter HTTP GET request.

        Args:
            twitterQuery: query object containing search parameters.

        Returns:
            json: partial query results containing matching tweets in json format,
                  from min_position to max_position
        """
        pass

    def _pretty_print(tweet):
        """
        Prints each non-private element of the tweet for debug.
        """
        for param in dir(tweet):
            if not param.startswith('_'):
                print "%s : %s\n" % (param, eval('tweet.' + param))


