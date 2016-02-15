import json
import pandas as pd
import tweepy
from tweepy import OAuthHandler


def main():
    """
    Connect to Twitter and get some tweets.
    """
    api = getTwitterAPI(getSecrets())

    edf_tweets, edf_t = getTweets(api, "edf", 100)
    eon_tweets, eon_t = getTweets(api, "eon", 100)
    bg_tweets, bg_t = getTweets(api, "britishgas", 100)
    np_tweets, np_t = getTweets(api, "npower", 100)

    edf_dataframe = getDataFrame(edf_tweets)

def getDataFrame(tweets):
    """
    Convert tweets in JSON format to Pandas' dataframe for easier data analysis.
    We are interested in location (see author location, author time zone and
    tweet's geolocation), description, ... ?
    (We also can use the Tweet's ID as the dataframe ID.)
    """
    dataframe = pd.DataFrame()

    dataframe['tweetID'] = [tweet.id for tweet in tweets]
    dataframe['tweetText'] = [tweet.text for tweet in tweets]
    dataframe['userLocation'] = [tweet.user.location for tweet in tweets]
    dataframe['userTimezone'] = [tweet.user.time_zone for tweet in tweets]
    dataframe['tweetCreated'] = [tweet.created_at for tweet in tweets]
    dataframe['userID'] = [tweet.user.id for tweet in tweets]
    dataframe['userScreen'] = [tweet.user.screen_name for tweet in tweets]
    dataframe['userName'] = [tweet.user.name for tweet in tweets]

    return dataframe

def getTweets(api, term, count):
    """
    Performs a search based on an entry term and returns a json object
    containing all matching tweets.
    """
    results = api.search(q=term, count=count)
    #How are r and results different? Tweepy Search vs Cursor
    r = []
    for tweet in tweepy.Cursor(api.search, q="edf").items(200):
        r.append(tweet)

    return results, r

def getTwitterAPI(secrets):
    """
    Use locally saved secrets to gain access to Twitter's API.
    """
    consumer_key = secrets['consumer_key']
    consumer_secret = secrets['consumer_secret']
    #access_token = secrets['access_token']
    #access_secret = secrets['access_secret']

    auth = OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_secret)

    return tweepy.API(auth)

def getSecrets():
    secrets = json.loads(open("secrets.json").read())
    return secrets

def pretty_print(tweet):
    """
    Prints each non-private element of the tweet for debug.
    """
    for param in dir(tweet):
        if not param.startswith('_'):
            print "%s : %s\n" % (param, eval('tweet.'+param))

if '__name__' == '__main__':
    main()
