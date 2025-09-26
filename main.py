# Assignment 2

import math
import statistics
import requests

API_key = ""
base_url = "https://restcountries.com/v3.1/"

country_name = input("What country are you interested in: ")

def country_search(country_name):
    url = f"{base_url}name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        country_info = response.json()
        return country_info
    else:
        print("Error: 404 not found")

print(country_search(country_name))

base_call = country_search(country_name)[0]

nativeName_dictkey = base_call['name']['nativeName'].keys()
nativeName_key = list(nativeName_dictkey)[0]

area = base_call['area']
capital = base_call['capital'][0]
english_name = base_call['name']['common'] 
local_name = base_call['name']['nativeName'][nativeName_key]['common']
population = base_call['population']
pop_density = population/area


print(area, capital, english_name, local_name, population, pop_density)





