# Example random_nr data stream
from data_stream import *
from random import random

def random_nr():
    return round(random()*10, 3)

random_nr_config = Config(_name = "Random Number Stream")
