# include new streams to start in this file

# add import
from data_streams.random_number import *
from data_streams.tcp_socket_client import *

from socket_server import SocketServer
from data_stream import *

import threading

def scheduler():
    """
    Start all streams
    """
    print("Flask up and running, now starting data streams...")

    # Start TCP socket Server
    SocketServer().start()

    # Start Example TCP socket client
    threading.Thread(target=test_client).start()

    # Start Example Random Number Stream
    DataStream(random_nr_config, random_nr).start()
