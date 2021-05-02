import time
import requests
from flask import Flask, render_template, request
from lang_dictionary import months_dict

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])

@app.route('/weather/en', methods=['GET', 'POST'])
def weather_en():
    weather = {}
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city = request.form.get('city')

    r = requests.get(url.format(city)).json()

    weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
        'wind_speed': r['wind']['speed'],
        'feels_like': r['main']['feels_like']
    }

    url2 = "http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1"

    r2 = requests.get(url2.format(city)).json()

    weather_list = []

    for i in range(0,30,7):
        epoch = r2['list'][i]['dt']
        date = time.strftime('%b %d', time.localtime(epoch))
        w = {
            'date': date,
            'temperature': r2['list'][i]['main']['temp'],
            'description': r2['list'][i]['weather'][0]['description'],
            'icon': r2['list'][i]['weather'][0]['icon'],
            'wind_speed': r2['list'][i]['wind']['speed'],
            'feels_like': r2['list'][i]['main']['feels_like']
        }

        weather_list.append(w)

    return render_template('weather.html', weather_list=weather_list, weather=weather)

@app.route('/weather/ru', methods=['GET', 'POST'])
def weather_ru():
    weather = {}
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&lang=ru&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city = request.form.get('city')

    r = requests.get(url.format(city)).json()

    weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
        'wind_speed': r['wind']['speed'],
        'feels_like': r['main']['feels_like']
    }

    url2 = "http://api.openweathermap.org/data/2.5/forecast?q={}&lang=ru&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1"

    r2 = requests.get(url2.format(city)).json()

    weather_list = []

    for i in range(0,30,7):
        epoch = r2['list'][i]['dt']
        date = time.strftime('%b %d', time.localtime(epoch))
        w = {
            'date': months_dict[date[0:3]] + date[3::],
            'temperature': r2['list'][i]['main']['temp'],
            'description': r2['list'][i]['weather'][0]['description'],
            'icon': r2['list'][i]['weather'][0]['icon'],
            'wind_speed': r2['list'][i]['wind']['speed'],
            'feels_like': r2['list'][i]['main']['feels_like']
        }

        weather_list.append(w)

    return render_template('weather-ru.html', weather_list=weather_list, weather=weather)

if __name__ == '__main__':
    app.run()
