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
        self.x, self.y, self.z = id # Axons base genration position
        # Length of axon and the position of each segment, max length that of column-z
        self.length_array = np.zeros((sv.layers['vi'][1], 3), dtype=int)
        self.length_array[0] = id # Sets starting position of axon afixed to neuron
        self.axon_head = 0 # The current length of the axon from base to head
        self.search_bias = self.define_bias() # Defines directional bias for growth


    def axonogenesis(self):
        print(sv.genesis_change.shape)
        print(self.search_bias)
        # Selects the direction of growth
        directional_selection = np.random.choice(sv.genesis_change, p=self.search_bias[0])
        
        # Selects the exact direction axon head will move
        narrow_direction = random.choices(directional_selection)

        print("Change: ", narrow_direction[0])
        print("Old: ", self.length_array[self.axon_head])
        print("Old: ", self.length_array[self.axon_head][0])
        print("Old: ", self.length_array[self.axon_head][1])
        print("Old: ", self.length_array[self.axon_head][2])

        # Computes new location from prevoius location
        new_location = narrow_direction + self.length_array[self.axon_head]

        print("New: ", new_location)
        self.axon_head = self.axon_head+1 # Increase axon in length
        
        self.length_array[self.axon_head] = new_location



    def define_bias(self):
        match self.layer:
            # Layer 'i' descending primarly to layer 'iv'
            case 'i': return sv.search_bias['descending']

            # Layer 'ii' locally descend & stays stagnates within the base layer
            case 'ii':
                return random.choices([sv.search_bias['local_descending'], sv.search_bias['stagnate']])

            # Layer 'iii' locally descends (Suppose to project out to other columns)
            case 'iii': return sv.search_bias['local']

            # Layer 'iv' ascends to layer 'i', 'ii' & 'iii'
            case 'iv':
                return random.choices([sv.search_bias['ascending'], sv.search_bias['local_ascending']])

            # Layer 'v' locally descend & descends (Suppose to project other columns)
            case 'v':
                return random.choices([sv.search_bias['local'], sv.search_bias['ascending']])

            # Layer 'vi' projects to
            case 'iv': return sv.search_bias['ascending']

            case _: return sv.search_bias['local']

