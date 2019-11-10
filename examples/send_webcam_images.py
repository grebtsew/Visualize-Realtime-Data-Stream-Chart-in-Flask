
from VisClient import VisClient
import time
import cv2
import base64

cap = cv2.VideoCapture(0)

conn = VisClient("127.0.0.1",12345)
print("Sending Images with one sec delay")
while True:
    ret, image = cap.read()

    retval, buffer = cv2.imencode('.png', image)
    encoded_string = "data:image/png;base64,"+base64.b64encode(buffer).decode()

    send_string = '{"id":69696969, "value":"'+encoded_string+'", "type":"image","name":"Webcam Stream"}'

    conn.send_large(send_string)

    time.sleep(1)

    #cv2.imshow("test", image)
    #cv2.waitKey(1)
