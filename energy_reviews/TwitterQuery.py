import datetime

"""
Query object containing all filter parameters and values that'll be used to
build the HTTP GET URL.
"""

class TwitterQuery:
    def __init__(self):
        self.search_terms = ''
        self.count = 0
        self.max_position = ''

    def set_search_terms(self, *args):
        """
        Main query string sent via HTTP GET request.
        Go through arguments to build it:
        q=arg1 OR arg2 is a valid q string
        """
        for arg in args:
            if args[0] == arg:
                self.search_terms += arg
            else:
                self.search_terms += " OR " + arg
        return self

    def set_count(self, count):
        """
        Number of tweets we want in the result.
        """
        self.count = count
        return self

    def set_since(self, since):
        """
        Start of query date range.
        """
        self._assert_date_valid(since)
        self.since = since
        return self

    def set_until(self, until):
        """
        End of query date range.
        """
        self._assert_date_valid(until)
        self.until = until
        return self

    def set_location(self, location):
        """
        Might be a geoname or a bounding box.
        """
        self.location = location
        return self

    def set_filter_user_out(self, username):
        """
        Ex. we want tweets about edfenergy, but excluding the ones that come
        from the edfenergy user since those filter out negative reviews.
        """
        self.filter_user_out = username
        return self

    def set_author(self, username):
        """
        Filter tweets from specific user. This could help working around the
        last 7-day restriction since Twitter API allows searching all tweets of
        a specific user.
        """
        self.author = username
        return self

    def set_min_position(self, min_position):
        """
        ID of oldest tweet being shown by Twitter in browser.
        """
        self.min_position = min_position
        return self

    def set_max_position(self, max_position):
        """
        ID of newest tweet being shown by Twitter in browser.
        """
        self.max_position = max_position
        return self

    def update(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

    def pretty_print(self):
        print "Twitter Query: "
        print " self.search_terms = " + self.search_terms
        print " self.count = " + str(self.count)
        print " self.since = " + self.since
        print " self.until = " + self.until
        print " self.filter_user_out = " + self.filter_user_out
        print " self.user = " + self.user
        print " self.location = " + self.location

    def _assert_date_valid(self, date):
        """
        Twitter API only accepts dates in format YYYY-MM-DD.
        """
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
