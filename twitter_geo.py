import tweepy

consumer_key = "x"
consumer_secret = "x"
access_key = "x"
access_secret = "x"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


if __name__ == '__main__':
    confirm = input()
    if confirm:
        with open('data/trends_date.txt', 'w', encoding='UTF-8', errors='ignore') as file:
            file.write(str(api.trends_place(1)))
