from sqlite3 import Time
from time import time
from django.shortcuts import render
from .models import *
from .utils import *
from Sports.newsApi import getNews
import requests
from .models import City
from .forms import CityForm, BaseballDateForm
import datetime
from Sports.API.weatherAPI import fetchWeather

def WeatherHome(request):
    dat = {}
    ctx = {'weather': dat, 'form': CityForm(), 'alert':{}}
    if request.method == 'POST':
        ctx['form'] = CityForm(request.POST)
        if ctx['form'].is_valid():
            city = ctx['form'].cleaned_data['name']
            weather = fetchWeather(city)
            ctx['weather'] = weather['weather']
            ctx['alerts'] = weather['alerts']

    return render(request, 'Sports/weather-home.html', ctx)


def BaseballPage(request):
    context = {}
    context['form'] = BaseballDateForm()
    
    if request.GET:
        temp = request.GET['date_field']
        date_string = populateBoxScores(temp)
    else:
        date_string = populateBoxScoresDefault()

    mlbGames = MlbBoxScoreData.objects.filter(date_played=date_string)
    context['mlbGames'] = mlbGames
    context['datePlayed'] = date_string
    return render(request, 'Sports/baseball.html', context)

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

def NewsHome_sort(request):
    if request.method == 'GET':
        sort_option = request.GET.get('option', None)

    context = getNews(sort_option)
    return render(request, 'Sports/news-home.html', context)
    
def SportsHome(request):
    return render(request, 'Sports/sports-home.html')

def BasketballPage(request):
    return render(request, 'Sports/basketball.html')
