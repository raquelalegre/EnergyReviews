import datetime

"""
Query object containing all filter parameters and values that'll be used to
build the HTTP GET URL.
"""

class TwitterQuery:
    def __init__(self):
        self.q = ''
        self.count = 0

    def set_q(self, *args):
        """
        Main query string sent via HTTP GET request.
        Go through arguments to build it:
        q=arg1 OR arg2 is a valid q string
        """
        for arg in args:
            self.q += " OR " + arg

    def set_count(self, count):
        """
        Number of tweets we want in the result.
        """
        self.count = count

    def set_since(self, since):
        """
        Start of query date range.
        """
        if _is_valid_date(since):
            self.since = since

    def set_until(self, until):
        """
        End of query date range.
        """
        if _is_valid_date(until):
            self.until = until

    def set_location(self, location):
        """
        Might be a geoname or a bounding box.
        """
        self.location = location

    def set_filter_user_out(self, username):
        """
        Ex. we want tweets about edfenergy, but excluding the ones that come
        from the edfenergy user since those filter out negative reviews.
        """
        self.filter_user_out = username

    def set_from(self, username):
        """
        Filter tweets from specific user. This could help working around the
        last 7-day restriction since Twitter API allows searching all tweets of
        a specific user.
        """
        self.from = username

    def set_min_position(self, min_position):
        """
        ID of oldest tweet being shown by Twitter in browser.
        """
        self.min_position = min_position

    def set_max_position(self, max_position):
        """
        ID of newest tweet being shown by Twitter in browser.
        """
        self.max_position = max_position

    def update(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

    def print(self):
        print "Twitter Query: "
        print " self.q = " + self.q
        print " self.count = " + self.count
        print " self.since = " + self.since
        print " self.until = " + self.until
        print " self.filter_user_out = " + self.filter_user_out
        print " self.user = " + self.user
        print " self.location = " + self.location

    def _is_valid_date(self, date):
        """
        Twitter API only accepts dates in format YYYY-MM-DD.
        """
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return True
