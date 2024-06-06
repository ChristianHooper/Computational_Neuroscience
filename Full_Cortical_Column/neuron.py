import time
import random
import numpy
from space import Space
import system_variables as sv

class Neuron(Space):
    def __init__(self, position, id, generation_number, layer):
        super().__init__()
        self.exists = 1
        self.id = id # String id for dictionarty lookup (controler/position_dictionary)
        self.layer = layer # Dictionary key for layer value
        self.generation_number = generation_number # Birth order value for batch.
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.color = self.depth_color()
        
        #self.color = sv.normalization(self.y, )

        # elf.dt = delta_time # Hundredth of a second delta_time base, only has one step to deal with peak gamma wave.
        # self.tau = tau # Rate of decay



    def depth_color(self):
        pre_color = sv.base_colors[self.layer] # Sets base color of neuron
        y_offset = self.y / 50
        post_color = tuple(y * y_offset +0.1 for y in pre_color)
        # Calculates multipler for y-axis depth, lower number the deeper
        # y_multiplier = tuple(sv.normalization(self.y, 0, 50) * x for x in pre_color)
        print(post_color)
        return post_color



# Get the measurement of time between the input time and the time when called.
def get_time(input_time): return (time.time() - input_time)

