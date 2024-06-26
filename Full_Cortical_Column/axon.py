import numpy as np
from space import Space
import system_variables as sv
import random

# 0528 bathroom code

class Axon(Space):
    def __init__(self, id, layer, type):
        super().__init__()
        self.exists = 1
        self.layer = layer # What layer the axon originates from
        self.id = id # id neuron axon is generated from, position tuple
        self.x, self.y, self.z = id # Axons base generation position
        # Length of axon and the position of each segment, max length that of column-z
        self.length_array = np.zeros((sv.layers['vi'][1], 3), dtype=int)
        self.length_array[0] = id # Sets starting position of axon afixed to neuron
        self.axon_head = 0 # The current length of the axon from base to head
        self.search_bias = self.define_bias() # Defines directional bias for growth
        self.growing = True # If the axon is currently growing


    def axonogenesis(self):
        # Selects a general cardinal direction based upon layer
        direction = random.choices((0,1,2,3,4,5), weights=self.search_bias)[0]

        # Selects a specific location for growth
        discrete_direction = random.randint(0, len(sv.genesis_change[direction]) -1)

        # Checks to make sure axon isn't growing outside of the bounds of the morpho-space
        if np.all(self.length_array[self.axon_head][0:2] < sv.layers['width']-1) and self.length_array[self.axon_head][1] < sv.layers['iv'][1]+1:

            # Increase length of axon array and increase `axon_head` length from soma
            self.length_array[self.axon_head+1] = self.length_array[self.axon_head] + sv.genesis_change[direction][discrete_direction]
            self.axon_head = self.axon_head+1

        print('Current: ', *self.length_array[self.axon_head])
        if sv.morphological_array[*self.length_array[self.axon_head]] == Space or Axon:
        # Unpacks new axon location and replaces empty space object with that axon
            print("growth")
            sv.morphological_array[*self.length_array[self.axon_head]] = self
        else: print("HIT"); self.growing = False


    def define_bias(self):
        match self.layer:
            # Layer 'i' descending primarily to layer 'iv'
            case 'i': return sv.search_bias['descending']

            # Layer 'ii' locally descend & stays stagnates within the base layer
            case 'ii':
                return random.choices([sv.search_bias['local_descending'], sv.search_bias['stagnate']])[0]

            # Layer 'iii' locally descends (Suppose to project out to other columns)
            case 'iii': return sv.search_bias['local']

            # Layer 'iv' ascends to layer 'i', 'ii' & 'iii'
            case 'iv':
                return random.choices([sv.search_bias['ascending'], sv.search_bias['local_ascending']])[0]

            # Layer 'v' locally descend & descends (Suppose to project other columns)
            case 'v':
                return random.choices([sv.search_bias['local'], sv.search_bias['ascending']])[0]

            # Layer 'vi' projects to
            case 'iv': return sv.search_bias['ascending']

            case _: return sv.search_bias['local']

