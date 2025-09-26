import requests

api_key = 'zpka_f23faa02a4db4dc8a04ab0297aad62d0_bfb62b0bf'  # este es un ejemplo de la clave API, no es real
params = {'apikey': api_key, 'q': 'New York'}

aw_location_url = "https://dataservice.accuweather.com/currentconditions/v1/349727"
aw_location_res = requests.get(aw_location_url, params=params)

import pprint

pprint.pprint(aw_location_res.json())