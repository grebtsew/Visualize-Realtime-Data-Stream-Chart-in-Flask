from VisClient import VisClient
import time
import base64
import random


"""
This Function is under development and is not currently working!
"""
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import cv2

pixels = np.zeros((1080, 1920))

data_heat_value = 1


conn = VisClient("127.0.0.1",12345)
print("Creating and sending heatmap to server!!!")
while True:
    # Add 100 points
    for i in range(0,100):
    # Add random point in heatmap
        pixels[random.randint(0,1080-1)][random.randint(0,1920-1)] += data_heat_value
    fig, ax = plt.subplots()

    im = ax.imshow(pixels)


    ax.set_title("Heatmap Example")
    fig.tight_layout()

    fig.canvas.draw()

    #plt.show()

    image = np.array(fig.canvas.renderer._renderer)

    #cv2.imshow("test", image)
    #cv2.waitKey(1)

    retval, buffer = cv2.imencode('.png', image)
    encoded_string = "data:image/png;base64,"+base64.b64encode(buffer).decode()

    send_string = '{"id":696969969, "value":"'+encoded_string+'", "type":"image","name":""}'

    plt.close(fig)

    conn.send_large(send_string)

    time.sleep(2)
