
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
        'id':223322,
        'value':[round(random()*100, 3)],
        'type':'line',
        'active_points': 20,
        'label':['Random Number'],
        'legend': ['random'],
        'name':'Random Number Example',
        'borderColor':['#3e95cd'],
        'backgroundColor':['#3e95cd'],
        'api_crypt':CRYPT
        }
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

while True:
    print("Sending our POST request to server ...")
    print(API_ENDPOINT, data)
    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = json.dumps(data), headers=headers)


    time.sleep(5)
