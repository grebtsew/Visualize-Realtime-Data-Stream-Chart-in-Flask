from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context

import time

import functools
import webbrowser

import json

from random import random
from time import sleep

import threading
from threading import Thread, Event
from datetime import datetime

import socket
from http.server import HTTPServer, BaseHTTPRequestHandler


app = Flask(__name__)
app.config['DEBUG'] = False

#turn the flask app into a socketio app
socketio = SocketIO(app)

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()

port = 5000
url = "http://127.0.0.1:{0}".format(port)

class Config():
    # Describes the visuals of graphs
    def __init__(self, _id= 0, _type = 'line', _active_points = 20, _delay = 1, _name = "RealtimeGraph", _label="data", _legend="data", _width = 200, _height = 100):
        self.type = _type
        self.active_points = _active_points
        self.delay = _delay = 1;
        self.id = _id
        self.name = _name
        self.label = _label
        self.legend = _legend
        self.width = _width
        self.height = _height

def random_nr():
    return round(random()*10, 3)

class DataStream(Thread):
    def __init__(self, _config, _data_func):
        super(DataStream, self).__init__()
        self.data_func = _data_func
        self.config = _config

    def run(self):
        while not thread_stop_event.isSet():
            socketio.emit('server',
            {'id':threading.current_thread().ident + self.config.id,
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
             'value': self.data_func(),
             'type': self.config.type,
             'active_points': self.config.active_points,
             'label': self.config.label,
             'legend': self.config.legend,
             'name': self.config.name,
             'width': self.config.width,
             'heigth': self.config.height},
              namespace='/test')
            sleep(self.config.delay)

def send_request(id, data, type = 'line', active_points = 20):
    socketio.emit('server',
    {'id': id,
    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
     'value': data,
     'type': type,
     'active_points': active_points},
      namespace='/test')

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
                        print(data)
                        djson = json.loads(data)
                        send_request(id = data["id"], data=data["value"])

def test_client():
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = (HOST, PORT)

    sock.connect(server_address)

    while True:
        sock.sendall(str.encode('{"id":10, "value": '+str(round(random()*10, 3))+', "type":"line","active_points": 20 }'))
        time.sleep(2)

def scheduler():
    # Random Number Stream
    DataStream(Config(), random_nr).start()
    # TCP socket Server example
    SocketServer().start()
    threading.Thread(target=test_client).start()
    # UDP socket example

    # HTTP server example

    # bluetooth example

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        scheduler()


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    threading.Timer(1, functools.partial( webbrowser.open, url )).start()
    socketio.run(app)
