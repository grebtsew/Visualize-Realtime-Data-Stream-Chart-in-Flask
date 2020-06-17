
# importing the requests library
import requests
import time
from random import random
import json

# defining the api-endpoint
API_ENDPOINT = "http://127.0.0.1:8030"

CRYPT = "password-1"

# data to be sent to api

data = {
        'id':151515,
        'value':'{ center: {lat: 41.40338, lng: 2.17403}, zoom: 4, data: [{lat: 41.40334, lng: 2.17404},{lat: 41.40335, lng: 2.17407} ] }' ,
        'type':'map',
        'name':'Geo Marker Map Example',
        'api_crypt':CRYPT
        }
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

while True:
    print("Sending our POST request to server ...")
    print(API_ENDPOINT, data)
    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = json.dumps(data), headers=headers)


    time.sleep(15)
