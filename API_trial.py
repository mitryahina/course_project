# This module shows the capacities of News API
from newsapi import NewsApiClient

# Initializing
newsapi = NewsApiClient(api_key='ce605f777cfe45f7883bdebddc674fed')


def get_headlines():
    # getting top headlines
    return newsapi.get_top_headlines(q='bitcoin', language='en')



def get_all_articles():
    # looking for all articles
    all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_parameter='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
    return all_articles


def sources():
    # extracting sources
    return newsapi.get_sources()


if __name__ == '__main__':
    print(get_headlines())
    print(get_all_articles())
    print(sources())
