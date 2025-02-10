"""
All required libraries 
"""

import requests
import json

# My_API_Key = 'b50d23c7cc3b81d32d3abfdad0312a5c'
# Base_Url = "https://openweathermap.org/api/one-call-3.0/"

"""
Class that consist of four methods with task of fetching four different API calls Which are 
1) Current and forecasts weather data
https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

2) Weather data for any timestamp
https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={API key}

3) Daily aggregation
https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={lat}&lon={lon}&date={date}&appid={API key}

4) Weather overview
https://api.openweathermap.org/data/3.0/onecall/overview?lat={lat}&lon={lon}&appid={API key}

"""
class Wheather:

    def get_current_and_forecast_weather(self):
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=67&lon=78.7&appid=b50d23c7cc3b81d32d3abfdad0312a5c")
        data_first = response.json()

        with open(r"D:\apexa_webscrspping\REST_API_DAY4\first.json", "w") as file:
           json.dump(data_first, file, indent=4) 

        return data_first
obj = Wheather()
print(obj.get_current_and_forecast_weather())