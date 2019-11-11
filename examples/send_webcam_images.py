
from VisClient import VisClient
import time
import cv2
import base64
import threading


class sender(threading.Thread):
    def __init__(self, conn, image):
        super(sender,self).__init__()
        self.done = True
        self.conn = conn
        self.image = image
    def is_done(self):
        return self.done

    def run(self):
        self.done = False
        retval, buffer = cv2.imencode('.png', self.image)
        encoded_string = "data:image/png;base64,"+base64.b64encode(buffer).decode()
        send_string = '{"id":69696969, "value":"'+encoded_string+'", "type":"image","name":"Webcam Stream"}'
        self.conn.send_large(send_string)
        self.done = True



cap = cv2.VideoCapture(0)
conn = VisClient("127.0.0.1",12345)
extra_thread = None
print("Sending Images with one sec delay")
while True:
    time.sleep(2)
    ret, image = cap.read()

    if extra_thread is None:
        extra_thread = sender(conn, image)
        extra_thread.start()
    else:

        if extra_thread.is_done() :
            extra_thread = sender(conn, image)
            extra_thread.start()

    #time.sleep(1)

    #cv2.imshow("test", image)
    #cv2.waitKey(1)
