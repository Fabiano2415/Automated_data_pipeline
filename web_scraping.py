#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
import re
import json
import sqlalchemy as db
import keys


# In[3]:


# password_key =keys.password_keys
# print(password_key)


# ## Web scraping: collect demographical data

# In[5]:


# Source
cities = ["Frankfurt","Madrid","Paris"]
cities.reverse()

countries, populations, longs, lats = [], [], [], []

for city in cities:
    url = f"https://en.wikipedia.org/wiki/{city}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BS(response.content, "html.parser")
        for s in soup.select("table.infobox tbody tr th"):
                
            if s.text.startswith("Population"):
                for s in s.parent.find_next_siblings():
                    if "Metro" in s.text and "/" not in s.text:
                        population = s.select("td")[0].text
                        population = population.split("[")[0]
                        populations.append(population)
                        
            if s.text == "Country":
                country = s.next_sibling.get_text()
                countries.append(country.strip())
    
        for s in soup.select("table.infobox tbody tr td"):
            if s.text.startswith("Coordinates: "):
                long, lat = s.text.split("/")[-1].split(";")
                longs.append(long.strip())
                lats.append(lat.strip())
                
            
cities_df = pd.DataFrame({
    "city": cities,
    "country": countries,
    "population": populations,
    "longitude": longs,
    "latitude": lats
})
cities_df


# In[11]:


schema="wbs_data_engineer_project_db"   # name of the database you want to use here
host="wbs-project3-db.caddbxh0tp4u.eu-central-1.rds.amazonaws.com"      # to connect to your local server
user="admin"
password="password_key " # your password!!!!
port=3306
con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'


# In[12]:


cities_df.to_sql("cities_df",con=con,if_exists='append',index=False)


# In[ ]:




