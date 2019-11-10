import socket
import time
from random import random

"""
Stock price stream example for this program
"""

def main():
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432 # can change this if you want

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = (HOST, PORT)

    sock.connect(server_address)

    while True:

        send_str = '{"id":80085, "value":['+str(round(random()*100, 3))+'], "type":"line","active_points": 20, "label":["Random Number"], "legend": ["random"], "name":"Random Number Example",  "borderColor":["#3e95cd"], "backgroundColor" :["#3e95cd"]}'
        sock.sendall(str.encode(send_str))

        time.sleep(0.5)

if __name__ == '__main__':
    main()
