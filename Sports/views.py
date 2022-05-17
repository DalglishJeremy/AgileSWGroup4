from django.shortcuts import render

def Home(request):
	return render(request, 'Sports/home.html')

def NewsHome(request):
	return render(request, 'Sports/news-home.html')

def SportsHome(request):
	return render(request, 'Sports/sports-home.html')

def BaseballPage(request):
	return render(request, 'Sports/baseball.html')

def BasketballPage(request):
	return render(request, 'Sports/basketball.html')

def WeatherHome(request):
	return render(request, 'Sports/weather-home.html')
# Create your views here.
