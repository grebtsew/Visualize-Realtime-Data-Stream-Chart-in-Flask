from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context

import webbrowser

from random import random
from time import sleep

import threading
from threading import Thread, Event
from datetime import datetime


app = Flask(__name__)
app.config['DEBUG'] = True


socketio = SocketIO(app)

thread = Thread()
thread_stop_event = Event()

class RandomThread(Thread):
    keep_running = True

    def __init__(self):
        self.delay = 1
        super(RandomThread, self).__init__()


    def randomNumberGenerator(self):
        """
        Generate a random number every 1 second and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread?
        """
        #infinite loop of magical random numbers
        print("Making random numbers")
        while not self.keep_running:
            try :
                number = round(random()*10, 3)
                print(number)
                socketio.emit('server', {'id':threading.current_thread().ident,'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': number}
    , namespace='/test')
                sleep(self.delay)
            except Exception:
                pass

    def stop(self):
        self.keep_running = False

    def run(self):
        self.randomNumberGenerator()



class stream_scheduler():
    def __init__(self):
        print("hej")
        RandomThread().start()
"""
class flask_handler():
    def __init__(self):
        super(flask_handler, self).__init__()

    def run(self):
        global app, socketio
        socketio.run(app)

    @app.route('/')
    def index():
        #only by sending this page first will the client be connected to the socketio instance
        return render_template('index.html')

    @socketio.on('connect', namespace='/test')
    def test_connect():
        # need visibility of the global thread object

        print('Client connected')
        RandomThread().start()

        #stream_scheduler()

    @socketio.on('disconnect', namespace='/test')
    def test_disconnect():
        print('Client disconnected')

if __name__ == '__main__':
    flask_handler().run()
"""
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
        thread = RandomThread()
        thread.start()


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
