import time
import json
from threading import Thread, Event
import socket
from data_stream import send_request

"""
SocketServer is a multithreaded socket server
receiving n amount of connections and proxy the messages
to flask
"""

class SocketServer(Thread):
    def __init__(self):
        super(SocketServer, self).__init__()

    def handle_connection(self, conn):
        with conn:
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
                          _name = safe(data, "name"), fill = safe(data, "fill"), backgroundColor = safe(data, "backgroundColor"), borderColor = safe(data, "borderColor"))
                    except Exception as e:

                        print(data)
                        print(" WARNING: an error occured in socket_server: ", e)


    def run(self):
        from config_handler import ConfigHandler
        (HOST, PORT) = ConfigHandler().get_all("SocketServer") # pylint: disable=unbalanced-tuple-unpacking

        #HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        #PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((str(HOST), int(PORT)))
            s.listen()
            try:
                while True:
                    conn, addr = s.accept()
                    print('Connected by', addr)
                    Thread(target=self.handle_connection, args=(conn,)).start()
            except Exception as e:
                print(e)

def safe(json, value):
    try:
        return json[value]
    except Exception:
        return
