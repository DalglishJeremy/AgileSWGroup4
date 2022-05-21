from sqlite3 import Time
from time import time
from django.shortcuts import render
from .models import *
from Sports.newsApi import getNews


def Home(request):
    return render(request, 'Sports/home.html')

def NewsHome(request):
    input_value = 'null'
    context = getNews(input_value)
    return render(request, 'Sports/news-home.html', context)

def NewsHome_search(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)
    
    context = getNews(search_query)
    return render(request, 'Sports/news-home.html', context)

def SportsHome(request):
    return render(request, 'Sports/sports-home.html')

def BaseballPage(request):
	mlbGames = MlbBoxScoreData.objects.all()

	return render(request, 'Sports/baseball.html',
				{'mlbGames': mlbGames})

def BasketballPage(request):
	return render(request, 'Sports/basketball.html')

def WeatherHome(request):
    return render(request, 'Sports/weather-home.html')
# Create your views here.
