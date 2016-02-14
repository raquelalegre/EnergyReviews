import urllib

class QueryBuilder:
    def __init__(self, query):
        self.query = query

    def _build_url(self):
        """
        Elaborates Query URL to be sent by TwitterClient.
        """
        query_url = ''

        prefix = 'https://twitter.com/i/search/timeline?f=realtime&src=typd'

        query_params = ['q', 'since', 'until', 'location', 'from',
            'min_position', 'max_position']

        for param in query_params:
            if hasattr(self.query, param):
                query_url += '&' + param + '=' + getattr(self.query, param)

        #Encode query_url
        query_url = prefix + urllib.quote(query_url)

        return query_url

    def get_url(self):
        return self.url

    def print(self, url):
        print "URL is " + url
