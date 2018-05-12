from newsapi import NewsApiClient

# Initializing
newsapi = NewsApiClient(api_key='x')

import tweepy

consumer_key = "x"
consumer_secret = "x"
access_key = "x"
access_secret = "x"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
twitter_api = tweepy.API(auth)
