# Weather API Test
from weatherAPI import fetchWeather
def weatherTest(city):
    context = fetchWeather(city)

    return context

def run():
    """
    {'weather': {
        'city': 'Philadelphia', 
        'temperature': 78.76, 
        'description': 'Broken clouds', 
        'icon': 'http://openweathermap.org/img/w/04d.png', 
        'humidity': 50, 'pressure': 1005, 'country': 'US', 
        'sunrise': datetime.datetime(2022, 6, 9, 5, 31, 54), 
        'sunset': datetime.datetime(2022, 6, 9, 20, 28, 10), 
        'windspeed': 19.57}, 
    'alerts': {}}
    """
    ctx = weatherTest('Philadelphia')

    assert ctx['weather'] is not None

    assert ctx['weather']['city'] == 'Philadelphia', \
     f"Expected Philadelphia, got: {ctx['weather']['city']}"

    print(f"SUCCESS")

run()