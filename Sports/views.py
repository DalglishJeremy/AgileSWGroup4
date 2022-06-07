from sqlite3 import Time
from time import time
from django.shortcuts import render
from .models import *
from .utils import *
from Sports.newsApi import getNews
import requests
from .models import City
<<<<<<< HEAD
from .forms import CityForm, BaseballDateForm
=======
from .forms import CityForm
import datetime
>>>>>>> weathercss

def WeatherHome(request):
    city = ""
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7b59b05d3e410e80c65cd3a16e85f8e1'
    #alerts_url='https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&exclude=minutely,hourly,daily&appid=7b59b05d3e410e80c65cd3a16e85f8e1'
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['name']

    form = CityForm()
    city_weather = {}
    alerts = {}
    city_req = requests.get(url.format(city))
    if city_req.status_code == 200: # got valid city
        city_weather = city_req.json()
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'].capitalize(),
            'icon' : "http://openweathermap.org/img/w/{}.png".format(city_weather['weather'][0]['icon']),
            'humidity': city_weather['main']['humidity'],
            'pressure': city_weather['main']['pressure'],
            'country': city_weather['sys']['country'],
            'sunrise': datetime.datetime.fromtimestamp(city_weather['sys']['sunrise']),
            'sunset': datetime.datetime.fromtimestamp(city_weather['sys']['sunset']),
            'windspeed': city_weather['wind']['speed']
            }
        # alert_req = requests.get(alerts_url.format(city_weather['coord']['lat'], city_weather['coord']['lon']))
        # if alert_req == 200:
        #     alert_res = alert_req.json()
        #     alerts = {
        #         'alerts': alert_res['alerts']
        #     }
    else:
        weather = {}

    context = {'weather': weather, 'form': form, 'alerts': alerts}

    return render(request, 'Sports/weather-home.html', context)


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

def SportsHome(request):
    return render(request, 'Sports/sports-home.html')

def BasketballPage(request):
    return render(request, 'Sports/basketball.html')