from django.shortcuts import render

def Home(request):
	return render(request, 'Sports/home.html')

def NewsHome(request):
	return render(request, 'Sports/new-home.html')

def SportsHome(request):
	return render(request, 'Sports/sports-home.html')

def WeatherHome(request):
	return render(request, 'Sports/weather-home.html')
# Create your views here.
