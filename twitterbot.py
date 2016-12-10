# Twitter Bot Starter Kit: Bot 1

# This bot tweets three times, waiting 15 seconds between tweets.

# If you haven't changed credentials.py yet with your own Twitter
# account settings, this script will tweet at twitter.com/lacunybot

# Housekeeping: do not edit
import time

import tweepy
from credentials import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


# What the bot will tweet

tweetlist = ['Watering your lawn can reduce maintance!',
             'This is also a landscaping tip that you can use!',
             'The third tip is also that best tip you can find!']

for line in tweetlist:
    api.update_status(line)
    print(line)
    print('...')
    time.sleep(50) # Sleep for 15 seconds

print("All done!")


