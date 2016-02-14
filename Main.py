import energy_reviews

def main():
   client = energy_reviews.TwitterClient
   query = energy_reviews.TwitterQuery
   query.set_q("edf", "edfenergy", "edfenergycs")
   query.set_count(2000)
   query.set_since('2015-01-01')
   query.set_until('2016-02-20')
   tweets = client.get_tweets(query)

   for tweet in tweets:
       print "Tweet: " + tweet

   #energy_reviews.getTweets("eon")
   #energy_reviews.getTweets("npower")
   #energy_reviews.getTweets("BritishGas")

if __name__ == '__main__':
        main()
