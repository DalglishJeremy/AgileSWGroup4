from sqlite3 import Time
from time import time
from django.shortcuts import render
from newsapi import NewsApiClient
import time

def Home(request):
    return render(request, 'Sports/home.html')

def NewsHome(request):

    currentDate = time.strftime("%Y-%m-%d")
    newsapi = NewsApiClient(api_key='fbfba5ccce3947d7987f287a603127c0')

    all_articles = newsapi.get_everything(q='football OR baseball OR golf OR basketball',
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
    return render(request, 'Sports/news-home.html', context)

def SportsHome(request):
    return render(request, 'Sports/sports-home.html')

def BaseballPage(request):
	return render(request, 'Sports/baseball.html')

def BasketballPage(request):
	return render(request, 'Sports/basketball.html')

def WeatherHome(request):
    return render(request, 'Sports/weather-home.html')
# Create your views here.
