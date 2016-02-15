"""
Represent a tweet with all the arguments we need.
"""

class Tweet:

    def __init__(self, status):
        self.text = status.text
        self.author = status.user.screen_name
        self.created_at = status.created_at
        self.id = status.id
        self.location = status.user.location
        self.time_zone = status.user.time_zone
        self.geo = status.geo
        self.lang = status.lang

    def pretty_print(tweet):
        """
        Prints each non-private element of the tweet for debug.
        """
        for param in dir(tweet):
            if not param.startswith('_'):
                print "%s : %s\n" % (param, eval('tweet.' + param))
