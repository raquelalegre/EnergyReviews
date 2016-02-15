from energy_reviews.client import TwitterClient
from energy_reviews.model import Tweet

def main():
   client = TwitterClient()

   result = client.api.get_status(585447362870571008)

   tweet = Tweet(result)

   tweet.pretty_print()

   #query = TwitterQuery
   #tweets = client.get_tweets(query)
   #query = energy_review.TwitterQuery
   #query = energy_review.TwitterQuery.set_q("edfenergy")
   #tweets = client.get_tweets(query)
   #for tweet in tweets:
   #    print "Tweet: " + tweet

   #energy_reviews.getTweets("eon")
   #energy_reviews.getTweets("npower")
   #energy_reviews.getTweets("BritishGas")
   pass


if __name__ == '__main__':
        main()
