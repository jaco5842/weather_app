import requests
import datetime

def get_weather_data(city):
    api_key = 'd89c10acc09aa2c7e50388895362b52f'
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        visibility = data['visibility']
        wind_speed = data['wind']['speed']
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']

        # Convert temperature values to Celsius
        temp_celsius = temp - 273.15
        feels_like_celsius = feels_like - 273.15
        temp_min_celsius = temp_min - 273.15
        temp_max_celsius = temp_max - 273.15

        # Convert visibility to kilometers
        visibility_km = visibility / 1000

        # Convert sunrise and sunset timestamps to formatted time
        sunrise_datetime = datetime.datetime.fromtimestamp(sunrise)
        sunset_datetime = datetime.datetime.fromtimestamp(sunset)
        sunrise_time = sunrise_datetime.strftime("%H:%M")
        sunset_time = sunset_datetime.strftime("%H:%M")

        # Return the weather data as a dictionary
        return {
            'temp_celsius': temp_celsius,
            'feels_like_celsius': feels_like_celsius,
            'temp_min_celsius': temp_min_celsius,
            'temp_max_celsius': temp_max_celsius,
            'pressure': pressure,
            'humidity': humidity,
            'visibility_km': visibility_km,
            'wind_speed': wind_speed,
            'sunrise_time': sunrise_time,
            'sunset_time': sunset_time
        }
    
    else:
        return None
