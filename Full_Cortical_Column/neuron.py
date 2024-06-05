import time
import random
import numpy



class Neuron():
    def __init__(self, x_pos, y_pos, z_pos):
        self.x = x_pos
        self.y = y_pos
        self.z = z_pos


        # elf.dt = delta_time # Hundredth of a second delta_time base, only has one step to deal with peak gamma wave.
        # self.tau = tau # Rate of decay





# Get the measurement of time between the input time and the time when called.
def get_time(input_time): return (time.time() - input_time)

