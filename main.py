import requests

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


country_info = country_search(country_name)
      
english_name = country_search(country_name)[0]['name']['common']

base_call = country_search(country_name)[0]

nativeName_dictkey = base_call['name']['nativeName'].keys()
nativeName_key = list(nativeName_dictkey)[0]

area = base_call['area']
capital = base_call['capital'][0]
english_name = base_call['name']['common'] 
local_name = base_call['name']['nativeName'][nativeName_key]['common']
population = base_call['population']
pop_density = population/area

def console_output():
    print(f"You selected: {english_name}")
    print(f"Native Name: {local_name}")
    print(f"Capital City: {capital}")
    print(f"Population: {population}")
    print(f"Area: {area} km2")
    print(f"Population Density: {round(pop_density)} km-2")

console_output()


# base_url = "https://restcountries.com/v3.1/all"

# def country_search():
#     url = f"{base_url}?fields=name,capital,area,population"
#     response = requests.get(url)

#     if response.status_code == 200:
#         country_info = response.json()
#         return country_info
#     else:
#         print("Error: 404 not found")

# print(country_search()[1])

# def parce_json():
#     for index, value in enumerate(country_info):
#         print((country_info[index]['name']['common']), country_info[index]['area'], country_info[index]['population'])

# parce_json()

# country_library = {}

# def build_the_library():
#     for index, value in enumerate(country_info):
#         pop_density = round((country_info[index]['population'])/(country_info[index]['area']), 0)
#         country_library.update({country_info[index]['name']['common']: {"Native Name": "local_name", "Capital City": "capital", "Population": country_info[index]['population'], "Area": country_info[index]['area'], "Population Density": pop_density}})

# build_the_library()


# for i in country_library:
#     print(i)


# print(country_library)
