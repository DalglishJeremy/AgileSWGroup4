from newsapi import NewsApiClient
import time


def getNews(input_value):
    currentDate = time.strftime("%Y-%m-%d")
    newsapi = NewsApiClient(api_key='fbfba5ccce3947d7987f287a603127c0')

    if(input_value != 'null'):
        query = input_value
    else:
        query = 'football OR baseball OR golf OR basketball OR Golf OR NFL OR NBA OR Hockey'

    all_articles = newsapi.get_everything(q=query,
                                      from_param='2022-05-16',
                                      to=currentDate,
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

    articles = all_articles['articles']
    length = len(articles)
    desc =[]
    title =[]
    img =[]
    artURL = []
    for i in range(length):
        f = articles[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        artURL.append(f['url'])


    mylist = zip(title, desc, img, artURL)
    context = {'mylist': mylist}
    return context