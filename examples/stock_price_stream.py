import socket
import time

from yahoo_fin import stock_info as si

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
        # get live price of Apple
        apple = si.get_live_price("aapl")

        # or Amazon
        amazon = si.get_live_price("amzn")

        print("apple: " ,apple,"amazon: ", amazon)

        send_str = '{"id":1337, "value": ['+str(apple)+', '+ str(amazon)+'], "type":"line","active_points": 20, "label":"Share Price ($)", "legend": ["apple", "amazon"], "name":"Stock Share Prices Example",  "borderColor":["#3e95cd", "#e8c3b9"], "backgroundColor" :["#3e95cd","#e8c3b9"]}'
        sock.sendall(str.encode(send_str))

        time.sleep(2)

if __name__ == '__main__':
    main()
