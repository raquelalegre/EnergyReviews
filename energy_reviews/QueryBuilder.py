import urllib
import urlparse

class QueryBuilder:
    def __init__(self, query):
        self.query = query

    def _build_url(self):
        """
        Elaborates Query URL to be sent by TwitterClient.
        """

        q = ''
        q_params = ['location', 'from', 'since', 'until']
        for param in q_params:
            if hasattr(self.query, param):
                q += ' ' + param + ':' + getattr(self.query, param)
        q = q + ' ' + self.query.search_terms
        q = urllib.quote(q)

        scheme='https'
        netloc='twitter.com'
        path='/i/search/timeline'
        params=''
        query='f={}&q={}&src={}&max_position={}'.format('realtime', q, 'typd', self.query.max_position)
        fragment=''

        self.url = urlparse.urlunparse((scheme, netloc, path, params, query, fragment))

    def get_url(self):
        self._build_url()
        self.pretty_print()
        return self.url

    def pretty_print(self):
        print "URL is " + self.url
