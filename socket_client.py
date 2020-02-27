import socket
import time
from threading import Thread

"""
This simple socket client
connects to our socket server and sends live stream numbers
to be displayed in flask.
"""

class SocketClient(Thread):

    def __init__(self, message):
        super(SocketClient, self).__init__()
        self.message = message

    def run(self):
        from config_handler import ConfigHandler
        (HOST, PORT) = ConfigHandler().get_all("SocketServer") # pylint: disable=unbalanced-tuple-unpacking

        #HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        #PORT = 65432 # can change this if you want

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = (str(HOST), int(PORT))

        sock.connect(server_address)

        while True:
            sock.sendall(str.encode(self.message))
            time.sleep(2)
