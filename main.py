from flask_handler import start_flask_application, app
import webbrowser
import threading
import functools
from config_handler import ConfigHandler

"""
Start Program with this file by running "python3 start.py"
"""

[HOST, PORT] = ConfigHandler().get_all("Website") # pylint: disable=unbalanced-tuple-unpacking

url = "http://"+HOST+":{0}".format(PORT)

if __name__ == '__main__':
    threading.Timer(1, functools.partial( webbrowser.open, url )).start()
    start_flask_application()

