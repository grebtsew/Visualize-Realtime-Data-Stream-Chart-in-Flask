from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context

from threading import Thread, Event
from scheduler import *
from socket_server import SocketServer

"""
Flask handler manages the start and connection to Flask website/server.
"""

app = Flask(__name__)
app.config['DEBUG'] = False # let this be false to only start one webbrowser

#turn the flask app into a socketio app
socketio = SocketIO(app)

thread = Thread() # scheduler thread
thread_stop_event = Event()

def start_flask_application():
    socketio.run(app)

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Flask Client connected')

    #Start the generator threads only if the thread has not been started before.
    if not thread.isAlive():
        scheduler()


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Flask Client disconnected')
