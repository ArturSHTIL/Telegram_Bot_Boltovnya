from tokens import bot_tokens
import requests
import datetime


def get_weather(message) -> str:
    weather_token = bot_tokens.weather_token()
    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message}&appid={weather_token}&units=metric"
        )
        data = r.json()
        message = data['name']
        cur_weather = data['main']['temp']
        weather_description = data['weather'][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Oh no, Please look at the window, your weather outside! "
        cur_humidity = data['main']['humidity']
        cur_pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sun_set = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])

        return (f"***** {datetime.datetime.now().strftime('%Y-%m-%d')} *****\n"
                f"Weather in a: {message}\nTemperature: {cur_weather}°C {wd}\n"
                f"Humidity: {cur_humidity}%\nPressure: {cur_pressure}\n"
                f"Wind: {wind} m/s\nSunrise: {sunrise_timestamp}\nSunset: {sun_set}\n"
                f"Length of the day: {length_of_day}")

    except:
        return 'Please Check the City'
