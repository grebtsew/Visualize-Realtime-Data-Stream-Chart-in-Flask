import time
import json

from threading import Thread, Event
from data_stream import *

from flask_handler import *
import socket

class SocketServer(Thread):
    def __init__(self):
        super(SocketServer, self).__init__()

    def run(self):
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    else:
                        #print(data)
                        try:
                            data = json.loads(data)
                            send_request(id = data["id"], data=data["value"], type =safe(data, "type"), active_points =safe(data, "active_points"),
                             _label=safe(data, "label"), _legend=safe(data, "legend"), _width = safe(data, "width"), _height = safe(data, "height"),
                              _name = safe(data, "name"))
                        except Exception as e:
                            print(" WARNING: an error occured", e)

def safe(json, value):
    try:
        return json[value]
    except Exception:
        return
