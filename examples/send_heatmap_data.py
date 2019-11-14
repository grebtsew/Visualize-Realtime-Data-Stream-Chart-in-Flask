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
    print("start Sending data")
    while True:
        point = (int(round(random()*192, 3)),int(round(random()*108, 3)))
        send_str = '{"id":80085, "value":['+str(point[0])+","+str(point[1])+'], "type":"heatmap","active_points": 20, "width":192, "height":108, "label":["Random Number"], "legend": ["random"], "name":"Random Pos Heatmap",  "borderColor":["#3e95cd"], "backgroundColor" :["#3e95cd"]}'
        sock.sendall(str.encode(send_str))

        time.sleep(1)

if __name__ == '__main__':
    main()
