# Import Modules
import tweepy
import pandas_datareader.data as data
import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from os import environ
from dotenv import load_dotenv

from currencies.main import get_prices, prices
from history.main import get_history_events

load_dotenv()

# Set up Twitter API
with open('../keys.txt') as f:
    content = f.read().splitlines()

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Getting different data
get_prices(data)            # get currencies and their prices
get_history_events(requests, BeautifulSoup)

# The actual currencies tweet
def tweet_currencies(prices):
    # api.update_status(status = f"Bitcoin: ${prices[0]}    #bitcoin\nEthereum: ${prices[1]}    #ethereum\nDogecoin: ${prices[2]}    #dogecoin\n\n$ Dollar: {prices[3]} Kč    #dollar\n€ Euro: {prices[4]} Kč    #euro\n\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\n\nsource code: https://github.com/ton1czech/gingy")
    print(prices[1])

def tweet_history_events(title, facts):
    print(title, facts)

tweet_currencies(prices)
tweet_history_events(title, facts)
# Schedule the processes
# sched = BlockingScheduler()

# @sched.scheduled_job('cron', hour='0,12')
# def timed_job():
#     tweet_currencies(prices)

# sched.start()