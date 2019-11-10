"""
This Class uses the flask visualization repo to show data
"""
import threading
import socket
import struct
import pickle
import cv2

class VisClient(threading.Thread):
    """
    This client sends images for detection server
    """

    def __init__(self, address,port):
        super(VisClient,self).__init__()
        self.address = address
        self.port = port
        self.s = socket.socket()
        self.s.connect((self.address,self.port))
        self.encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]


    def send_large(self,frame):

        data = pickle.dumps(frame, 0)
        size = len(data)
        #print("Sending Image of size ", size)
        self.s.sendall(struct.pack(">L", size) + data)

    def send(self, data):
        """
        Send data to vis
        """
        self.s.sendall(str.encode(data))

    def run(self):
        self.send()
