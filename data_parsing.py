from config import newsapi, twitter_api


def get_trends_names(location = 23424976):
    trends = twitter_api.trends_place(location)[0].get('trends')
    name_trends = []
    for i in trends:
        name_trends.append(i.get('name'))
    return name_trends


def get_news_headlines():
    news = newsapi.get_top_headlines(country='ua').get('articles')
    titles = []
    for i in news:
        titles.append(i.get('title'))
    return titles


print(get_news_headlines())
print(get_trends_names())
