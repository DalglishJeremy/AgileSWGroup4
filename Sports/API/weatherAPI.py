import datetime
import requests

def fetchWeather(in_city):
    city = in_city
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7b59b05d3e410e80c65cd3a16e85f8e1'
    #alerts_url='https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&exclude=minutely,hourly,daily&appid=7b59b05d3e410e80c65cd3a16e85f8e1'
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
            'windspeed': city_weather['wind']['speed'],
            'coordlat': city_weather['coord']['lat'],
            'coordlon': city_weather['coord']['lon']
            }
        # alert_req = requests.get(alerts_url.format(city_weather['coord']['lat'], city_weather['coord']['lon']))
        # if alert_req == 200:
        #     alert_res = alert_req.json()
        #     alerts = {
        #         'alerts': alert_res['alerts']
        #     }
    else:
        weather = {}

    context = {'weather': weather, 'alerts': alerts}

    return context