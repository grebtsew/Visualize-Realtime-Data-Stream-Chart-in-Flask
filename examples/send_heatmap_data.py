from VisClient import VisClient
import time
import base64
import random


"""
This Function is under development and is not currently working!
"""

print("THIS PROGRAM IS NOT CURRENTLY WORKING!!!!")
conn = VisClient("127.0.0.1",12345)
print("Sending heatmap data")
while True:
    size = (1920,1080)

    new_point =  (random.randint(0,size[0]), random.randint(0,size[1]))

    send_str = '{"id":80085, "value":['+str(round(random()*100, 3))+'], "type":"line","active_points": 20, "label":["Random Number"], "legend": ["random"], "name":"Random Number Example",  "borderColor":["#3e95cd"], "backgroundColor" :["#3e95cd"]}'

    send_string = '{"id":69696969, "value":"'+encoded_string+'", "type":"image","name":"Webcam Stream"}'

    conn.send(send_string)

    time.sleep(1)

    #cv2.imshow("test", image)
    #cv2.waitKey(1)
