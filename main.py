# Import Modules
import tweepy
import pandas_datareader.data as data
import datetime as dt
from apscheduler.schedulers.blocking import BlockingScheduler

# Set up Twitter API
with open('keys.txt') as f:
    content = f.read().splitlines()

consumer_key = content[0]
consumer_secret = content[1]
access_token = content[2]
access_token_secret = content[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get real-time prices
prices = []
price = data.get_quote_yahoo(['BTC-USD', 'ETH-USD', 'DOGE-USD', 'CZK=X', 'EURCZK=X'])['price']
for currency in price:
    currency = format(currency, ",.3f")
    prices.append(currency)

# The actual tweet
def write_tweet(prices):
    api.update_status(status = f"Bitcoin: ${prices[0]}    #bitcoin\nEthereum: ${prices[1]}    #ethereum\nDogecoin: ${prices[2]}    #dogecoin\n\n$ Dollar: {prices[3]} Kč    #dollar\n€ Euro: {prices[4]} Kč    #euro\n\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\n\nsource code: https://github.com/ton1czech/gingy")

# Schedule the process
sched = BlockingScheduler()

@sched.scheduled_job('cron', hour='0,12')
def timed_job():
    write_tweet(prices)

sched.start()