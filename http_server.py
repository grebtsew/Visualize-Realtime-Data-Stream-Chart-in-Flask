"""
This server will receive HTTP post requests and send the data to flask
"""
from threading import Thread
from data_stream import *
import http.server
from flask_handler import *
import json
from functools import partial
from http.server import BaseHTTPRequestHandler, HTTPServer

class S(BaseHTTPRequestHandler):
    CRYPT = "password-1"
    connection_list = []


    def _set_response(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS, HEAD, GET')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_response()

    def do_OPTIONS(self):
        self._set_response()

    def do_POST(self):
        #print(self.client_address,self.headers)

        if self.headers['Content-Length']:

            content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
            post_data = self.rfile.read(content_length) # <--- Gets the data itself
            #data = simplejson.loads(post_data)
            #print(post_data)
            # decode incoming data // see if password is correct here!

            data = json.loads(post_data)
            if data['api_crypt'] :
                if data['api_crypt'] == self.CRYPT:
                    
                    send_request(id = data["id"], data=data["value"], type =safe(data, "type"), active_points =safe(data, "active_points"),
                    _label=safe(data, "label"), _legend=safe(data, "legend"), _width = safe(data, "width"), _height = safe(data, "height"),
                    _name = safe(data, "name"), fill = safe(data, "fill"), backgroundColor = safe(data, "backgroundColor"),
                    borderColor = safe(data, "borderColor"))

        self._set_response()

class HTTPserver(Thread):

    PORT = 8000

    def __init__(self):
        super().__init__()

    def run(self):
        server_address = ('localhost', self.PORT)
        httpd = HTTPServer(server_address,S)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()

def safe(json, value):
    try:
        return json[value]
    except Exception:
        return
