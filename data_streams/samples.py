# Example random_nr data stream
from data_stream import Config
from random import random
from random import randrange

"""
Random generator working on this pc
"""
def random_nr():
    return [round(random()*10, 3)]

random_nr_config = Config(_name = "Random Number Stream")

"""
These are sample requests send via tcp sockets
"""

def random_color():
    color = [randrange(255),randrange(255),randrange(255)]
    return color

samplelist = []

samplelist.append('{"id":10, "value": ['+str(int(round(random()*10, 3)))+'], "type":"line","active_points": 20, "width":300, "height":150, "label":["value"], "legend":["legend"], "name":"line chart" }')
samplelist.append('{"id":20, "value": ['+str(round(random()*10, 3))+'], "type":"line","active_points": 20, "width":300, "height":150, "label":["value"], "legend":["legend"], "name":"line chart with full json", "fill": true, "backgroundColor":["#3e95cd"], "borderColor":["#3e95cd"]}')
samplelist.append('{"id":40, "value": ['+str(round(random()*10, 3))+'], "type":"pie","active_points": 20, "width":300, "height":150, "label":["value"], "legend":["legend"], "name":"Pie chart", "fill": false, "backgroundColor":["#e8c3b9"], "borderColor":["#c45850"]}')
samplelist.append('{"id":30, "value": ['+str(round(random()*10, 3))+'], "type":"bar","active_points": 20, "width":300, "height":150, "label":["value"], "legend":["legend"], "name":"Bar chart", "fill": false, "backgroundColor":["#8e5ea2"], "borderColor":["#e8c3b9"]}')
samplelist.append('{"id":50, "value": ['+str(round(random()*10, 3))+'], "type":"radar","active_points": 20, "width":300, "height":150, "label":["value"], "legend":["legend"], "name":"Radar chart", "fill": false, "backgroundColor":["#8e5ea2"], "borderColor":["#c45850"]}')
samplelist.append('{"id":70, "value": ['+str(round(random()*10, 3))+'], "type":"doughnut","active_points": 20, "width":300, "height":150, "label":["value"], "legend":["legend"], "name":"Doughnut chart", "fill": false, "backgroundColor":["#3e95cd"], "borderColor":["#c45850"]}')
samplelist.append('{"id":80, "value": ['+str(round(random()*10, 3))+'], "type":"horizontalBar","active_points": 20, "width":300, "height":150, "label":["value"], "legend":["legend"], "name":"Horizontal Bar chart", "fill": false, "backgroundColor":["#3cba9f"], "borderColor":["#c45850"]}')
#samplelist.append('{"id":60, "value": ['+str(int(round(random()*10, 3)))+'], "type":"polarArea","active_points": 20, "width":300, "height":150, "label":["value"], "legend":["legend"], "name":"Polar Area chart", "fill": false, "backgroundColor":["#3cba9f"], "borderColor":["#c45850"]}')
