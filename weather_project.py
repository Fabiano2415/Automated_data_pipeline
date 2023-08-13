#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from datetime import datetime
import pytz
import sqlalchemy as db
import pymysql
import keys


# ## Collect Weather Data

# In[2]:


# List of cities
cities_list = ['Frankfurt', 'Paris', 'Madrid']

def get_weather_loop(cities):
    API_key = 'keys.weather_keys'
    tz = pytz.timezone('Europe/Berlin')
    now = datetime.now().astimezone(tz)
    
    weather_dict = {
        'city': [],
        'country': [],
        'forecast_time': [],
        'outlook': [],
        'temperature': [],
        'clouds': [],
        'wind_speed': [],
        'wind_deg': [],
        'humidity': [],
        'pressure': [],
        'information_retrieved_at': []
    }

    # API that provides free weather forecasts: OpenWeather.
    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}&units=metric"
        response = requests.get(url)
        json_data = response.json()

        # Loop through forecast entries in the JSON data
        for forecast in json_data['list']:
            # Get the city name from the JSON data (may be the full name)
            city_name = json_data['city']['name']
            
            # Check if the city name contains "am Main" and replace it with just "Frankfurt"
            if "am Main" in city_name:
                city_name = city_name.replace("am Main", "")
            
            weather_dict['city'].append(city_name)
            weather_dict['country'].append(json_data['city']['country'])
            weather_dict['forecast_time'].append(forecast['dt_txt'])
            weather_dict['outlook'].append(forecast['weather'][0]['main'])
            weather_dict['temperature'].append(forecast['main']['temp'])
            weather_dict['clouds'].append(forecast['clouds']['all'])
            weather_dict['wind_speed'].append(forecast['wind']['speed'])
            weather_dict['wind_deg'].append(forecast['wind']['deg'])
            weather_dict['humidity'].append(forecast['main']['humidity'])
            weather_dict['pressure'].append(forecast['main']['pressure'])
            weather_dict['information_retrieved_at'].append(now.strftime("%d/%m/%Y %H:%M:%S"))

    # Create a pandas DataFrame from the weather_dict
    weather_dataframe = pd.DataFrame(weather_dict)
    return weather_dataframe

weather_cities = get_weather_loop(cities_list)
#print(weather_cities)


# In[3]:


weather_cities


# In[4]:


schema="wbs_data_engineer_project_db"   # name of the database you want to use here
host="wbs-project3-db.caddbxh0tp4u.eu-central-1.rds.amazonaws.com"      # to connect to your local server
user="admin"
password="password_key " # your password!!!
port=3306
con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'


# In[5]:


weather_cities.to_sql("weather_cities",con=con,if_exists='append',index=False)


# In[ ]:




