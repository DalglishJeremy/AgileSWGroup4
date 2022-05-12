from django.shortcuts import render

def SportsHome(request):
	return render(request, 'Sports/sports-home.html')
# Create your views here.
