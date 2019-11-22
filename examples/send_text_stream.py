import socket
import time

"""
Stock price stream example for this program
"""
import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def main():
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432 # can change this if you want

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = (HOST, PORT)

    sock.connect(server_address)
    print("Start sending random text")
    while True:

        send_str = '{"id":80085, "value":"'+randomString(random.randint(1,50))+'", "type":"text","active_points": 20, "name":"Random Text Example",  "borderColor":["#ffffff"], "backgroundColor" :["#000000"]}'
        sock.sendall(str.encode(send_str))

        time.sleep(0.5)

if __name__ == '__main__':
    main()
