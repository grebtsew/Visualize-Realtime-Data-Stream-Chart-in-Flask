"""
This Demo demonstrates how to start a FFMPEG & GSTREAMER rtsp server of the webcam stream and send the address to
our Visualizer for visualization!
"""

address = "127.0.0.1"
port = 1337
webcam_name= "USB2.0 UVC 1M WebCam"
Use_FFMPEG= False

import os

print ("Starting server")

if Use_FFMPEG:
    # Create rtsp server for FFMPEG, require FFMPEG command installed on pc and a webcam!
    stream = os.popen('ffmpeg -f dshow -i video="'+webcam_name+'" -acodec libmp3lame -ar 11025 -f mpegts udp://'+address+":"+str(port))
else:
    # Create rtsp server for GSTREAMER, require GSTREAMER command installed on pc and a webcam!
    stream = os.popen('gst-launch-1.0 autovideosrc device=/dev/videoX ! video/x-raw,width=640,height=480,encoding-name=H264 ! videoconvert ! jpegenc ! udpsink host='+address+' port='+str(port))

# Use top or activity manager to shutdown the streams if you do not use debugmode! Pycharm loses childprocesses!

print("Stream active at :" +'udp://'+address+":"+str(port))

print("Sending stream address to Visulization Stream...")
video_data= {
    'id': 144124,
    'value': 'udp://'+address+":"+str(port),
    'type': 'video_stream',
    'name': 'Video Stream HTTP Example',
    'api_crypt':"password-1"}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
API_ENDPOINT = "http://localhost:8030" # set in config

import requests
import json
import time
while True:
# sending post request and saving response as response object
    requests.post(url=API_ENDPOINT, data=json.dumps(video_data), headers=headers)
    time.sleep(2)
            


"""
#Uncomment this if you want to test the rtsp server streams in this program!
import cv2
print(" Test Capture video ")
cap = cv2.VideoCapture("udp://"+address+":"+str(port))
# get list
while True:
    ret, frame = cap.read()

    cv2.imshow("test", frame)
    cv2.waitKey(1)
"""

while True:
    time.sleep(10) # keep thread alive

