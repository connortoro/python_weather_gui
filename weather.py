import pip._vendor.requests as requests
from dotenv import load_dotenv, find_dotenv
import os

# Get env variable for API key
load_dotenv(find_dotenv())
api_key = os.environ.get("WEATHER_API_KEY")


def get_weather(city):
    res = requests.get(
  f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

    if(res.status_code != 200):
        return "Error, bad response"

    weather_data = res.json()

    description = weather_data['weather'][0]['description']
    high = str(int(weather_data['main']['temp_max']))
    low = str(int(weather_data['main']['temp_min']))
    curr = str(int(weather_data['main']['temp']))

    return ("The weather in " + city + " is " + description + ", with a high of "
            + high + "F and a low of " + low + "F. The current temp is " + curr + "F")



