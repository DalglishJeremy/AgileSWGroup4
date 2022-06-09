"""NewsSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 

from Sports import views

urlpatterns = [
    path('admin/',              admin.site.urls,       name="admin"),
    path('',                    views.Home,            name="Home"),
    path('News/',               views.NewsHome,        name="News"),
    path('News/search',         views.NewsHome_search, name="News_search"),
    path('News/sorted',         views.NewsHome_sort,   name="News_sort"),
    path('Sports/',             views.SportsHome,      name="Sports"),
    path('Sports/Baseball',     views.BaseballPage,    name="Baseball"),
    path('Sports/Basketball',   views.BasketballPage,  name="Basketball"),
    path('Weather/',            views.WeatherHome,     name="Weather"),
]
