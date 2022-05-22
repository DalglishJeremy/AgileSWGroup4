from sqlite3 import Time
from time import time
from django.shortcuts import render
from .models import *
from Sports.newsApi import getNews
import requests
from .models import City
from .forms import CityForm

def WeatherHome(request):
    cities = City.objects.all()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7b59b05d3e410e80c65cd3a16e85f8e1'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
            'humidity': city_weather['main']['humidity'],
            'pressure': city_weather['main']['pressure'],
            'country': city_weather['sys']['country'],
            'sunrise': city_weather['sys']['sunrise'],
            'sunset': city_weather['sys']['sunset'],
            'windspeed': city_weather['wind']['speed']
        }

        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'Sports/weather-home.html', context)

def Home(request):
    return render(request, 'Sports/home.html')

def NewsHome(request):
    input_value = 'null'
    context = getNews(input_value)
    return render(request, 'Sports/news-home.html')

def NewsHome_search(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)
    
    context = getNews(search_query)
    return render(request, 'Sports/news-home.html')

def SportsHome(request):
    return render(request, 'Sports/sports-home.html')

def BaseballPage(request):
	mlbGames = MlbBoxScoreData.objects.all()

	return render(request, 'Sports/baseball.html',
				{'mlbGames': mlbGames})

def BasketballPage(request):
    return render(request, 'Sports/basketball.html')


