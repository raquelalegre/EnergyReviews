"""
Query object containing all filter parameters and values that'll be passed to
the HTTP GET request.
"""

class TwitterQuery:
    def __init__(self):
        pass

    def set_q(self, q_str):
        """
        Main query string sent via HTTP GET request.
        TODO: Can it containg several params?
              Ex. Tweets matching "edf" or edfenergy" or "edfenergyuk".
        """
        pass

    def set_count(self, count):
        """
        Number of tweets we want in the result.
        """
        pass

    def set_since(self, since):
        """
        Start of query date range.
        """
        pass

    def set_until(self, until):
        """
        End of query date range.
        """
        pass

    def set_location(self, location):
        """
        Might be a geoname or a bounding box.
        """
        pass

    def set_filter_user_out(self, username):
        """
        Ex. we want tweets about edfenergy, but excluding the ones that come
        from the edfenergy user since those filter out negative reviews.
        """
        pass

    def set_user(self, username):
        """
        Filter tweets from specific user. This could help working around the
        last 7-day restriction since Twitter API allows searching all tweets of
        a specific user.
        """
        pass
