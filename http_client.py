import requests
from threading import Thread
import json
import time
"""
This simple socket client
connects to our socket server and sends live stream numbers
to be displayed in flask.
"""

class HTTPClient(Thread):

    def __init__(self):
        super(HTTPClient, self).__init__()

    def run(self):
        from config_handler import ConfigHandler
        (HOST, PORT, CRYPT) = ConfigHandler().get_all("HTTPServer")

        data = {
            'id': 12,
            'value': 0,
            'type': 'video_stream',
            #'type': 'line',
            #'active_points': 20,
            #'label': ['Random HTTP Number'],
            #'legend': ['random'],
            'name': 'Video Stream HTTP Example',
            #'borderColor': ['#3e95cd'],
            #'backgroundColor': ['#3e95cd'],
            'api_crypt':CRYPT
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        API_ENDPOINT = "http://"+HOST+":"+PORT

        #while True:
        # sending post request and saving response as response object
        r = requests.post(url=API_ENDPOINT, data=json.dumps(data), headers=headers)
        time.sleep(2)

