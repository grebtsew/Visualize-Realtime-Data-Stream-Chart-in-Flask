# include new streams to start in this file

from data_streams.samples import *

from socket_client import SocketClient
from socket_server import SocketServer
from image_server import ImageServer
from data_stream import *
from http_server import HTTPserver

import threading

"""
Scheduler starts the SocketServer and local data streams when
 flask server is up and running.
"""

def scheduler():
    """
    Start all streams
    """
    print("Flask up and running, now starting data streams...")

    # Start TCP socket Server
    SocketServer().start()
    ImageServer().start()

    # Start HTTP server
    HTTPserver().start()

    # Can be a smart idea to start streams here!
    # Start some demo flows
    demo()

def demo():

    # Start Example TCP socket client
    for message in samplelist: # see samplelist in /data_streams/samples.py
        SocketClient(message=message).start()

    # Start Example Random Number Stream
    DataStream(random_nr_config, random_nr).start()
