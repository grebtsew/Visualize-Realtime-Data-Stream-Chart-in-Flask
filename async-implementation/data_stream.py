from threading import Thread
import flask_handler
from datetime import datetime
import time

# TODO: add color
# TODO: think about how to make all graphs useable

class Config():
    # Describes the visuals of graphs
    def __init__(self, _id= 0, _type = 'line', _active_points = 20, _delay = 1, _name = "RealtimeGraph", _label="Value", _legend="data", _width = 200, _height = 100):
        self.type = _type
        self.active_points = _active_points
        self.delay = _delay = 1;
        self.id = _id
        self.name = _name
        self.label = _label
        self.legend = _legend
        self.width = _width
        self.height = _height

class DataStream(Thread):
    def __init__(self, _config, _data_func):
        super(DataStream, self).__init__()
        self.data_func = _data_func
        self.config = _config

    def run(self):
        while not flask_handler.thread_stop_event.isSet():
            flask_handler.socketio.emit('server',
            {'id':self.config.id,
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
             'value': self.data_func(),
             'type': self.config.type,
             'active_points': self.config.active_points,
             'label': self.config.label,
             'legend': self.config.legend,
             'name': self.config.name,
             'width': self.config.width,
             'heigth': self.config.height},
              namespace='/test')
            time.sleep(self.config.delay)


def def_param(vari, deff):
    if vari is None:
        return deff
    else:
        return vari

def send_request(id, data, type = 'line', active_points = 20, _label="Value", _legend="data", _width = 200, _height = 100, _name = "Graph" ):
    type = def_param(type, 'line')
    active_points = def_param(active_points, 20)
    _label = def_param(_label, 'Value')
    _legend = def_param(_legend, 'data')
    _height = def_param(_height, 200)
    _width = def_param(_width, 100)
    _name = def_param(_name, 'Graph')

    flask_handler.socketio.emit('server',
    {'id': id,
    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
     'value': data,
     'type': type,
     'active_points': active_points,
     'label': _label,
     'legend': _legend,
     'name': _name,
     'width': _width,
     'heigth': _height},
      namespace='/test')
