from newsapi import NewsApiClient

# Initializing
newsapi = NewsApiClient(api_key='ce605f777cfe45f7883bdebddc674fed')

import tweepy

consumer_key = "oCP8hMSYpC0jZ8mYIoRjvdzic"
consumer_secret = "FoVR1k8OsoV1ygaB50cKawSFHOwVA1w2Wi2wKFsJkuAoQ7JNFH"
access_key = "963664485755031553-Oj2bWzLidS9VHCdzPSKrfInVfudpaRa"
access_secret = "ZqmIJVRoohgK2aI34OHggcs08OzQysW6s9Esz8wUXZ9SH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
twitter_api = tweepy.API(auth)
