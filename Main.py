import energy_reviews

def main():
   client = energy_reviews.TwitterClient
   query = energy_reviews.TwitterQuery
   #query = energy_review.TwitterQuery.set_q("edfenergy")
   #tweets = client.get_tweets(query)
   #for tweet in tweets:
   #    print "Tweet: " + tweet

   #energy_reviews.getTweets("eon")
   #energy_reviews.getTweets("npower")
   #energy_reviews.getTweets("BritishGas")


if __name__ == '__main__':
        main()


