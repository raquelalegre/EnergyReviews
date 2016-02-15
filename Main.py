from __future__ import print_function
import energy_reviews


def main():
   client = energy_reviews.TwitterClient()

   energy_accounts = {
    'edf': 'edfenergy',
    'eon': 'eonenergyuk',
    'british_gas': 'BritishGas',
    'npower': 'npower',
    'scottish_power': 'ScotishPower',
    'sse': 'SSE', 
    'souther_elec': 'southernelec',
    'ovo': 'OVOEnergy',
    'ecotricity': 'ecotricity',
    'ebico': 'ebicoltd',
    'utilita': 'UtilitaEnergy',
    'extra': 'extraenergyuk',
    'first': 'FirstUtility'
   }


   for company in energy_accounts:
       query = energy_reviews.TwitterQuery()
       query.set_search_terms(energy_accounts[company])
       query.set_count(5000)
       query.set_since('2014-01-01')
       query.set_until('2016-12-20')
       tweets = client.get_tweets(query)
       filename = company + ".log"
       f = open(filename, 'w')
       for tweet in tweets:
           print(tweet.message)
           print(tweet.username.encode('utf8') + ";" + tweet.message.encode('utf8'), file=f)
       f.close()




if __name__ == '__main__':
        main()
