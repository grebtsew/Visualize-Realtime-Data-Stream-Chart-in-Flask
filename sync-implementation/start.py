import json
import random
import time
from datetime import datetime
import threading
from flask import Flask, Response, render_template
import webbrowser
import time


# Application reference
application = Flask(__name__)

class Data_Stream:

    def __init__(id, filter_func, data):
        pass

class Data_Vizualiser:
    port = 5000
    url = "http://127.0.0.1:{0}".format(port)
    data_stream_list = []

    def __init__(self):
        pass

    def run(self):
        threading.Timer(1, lambda: webbrowser.open(self.url) ).start()
        application.run(debug=True, threaded=True)

    def add_data_stream(id, filter_func, data):
        data_stream_list.add(Data_Stream(id, filter_func, data));
        pass

    @application.route('/')
    def index():
        return render_template('index.html')

    @application.route('/server')
    def chart_data():
        def generate_random_data():

            while True:
                if(random.random() >= 0.5):
                    json_data = json.dumps(
                    {'id':1,'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': random.random() * 100})
                else:
                    json_data = json.dumps(
                    {'id':2,'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': random.random() * 100})

                yield f"data:{json_data}\n\n"
                time.sleep(0.01)
        return Response(generate_random_data(), mimetype='text/event-stream')



if __name__ == '__main__':
    shower = Data_Vizualiser()
    random.seed()  # Initialize the random number generator
    shower.run()
    time.sleep(3)
    print("start stream")
