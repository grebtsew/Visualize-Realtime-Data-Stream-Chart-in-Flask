import socket
from random import random
import time

"""
This simple tcp socket client
connects to our socket server and sends live stream random numbers
to be displayed in flask.
"""

def test_client():
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = (HOST, PORT)

    sock.connect(server_address)

    while True:
        sock.sendall(str.encode('{"id":10, "value": '+str(round(random()*10, 3))+', "type":"line","active_points": 20, "width":300, "height":150, "label":"label", "legend":"legend", "name":"name" }'))
        time.sleep(2)
