import time
import random
import numpy



class Neuron():
    def __init__(self, position):
        self.position_id = position
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]


        # elf.dt = delta_time # Hundredth of a second delta_time base, only has one step to deal with peak gamma wave.
        # self.tau = tau # Rate of decay





# Get the measurement of time between the input time and the time when called.
def get_time(input_time): return (time.time() - input_time)

