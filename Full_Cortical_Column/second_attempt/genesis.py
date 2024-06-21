import numpy as np
import controller as ct
import random
from space import Space
import project_variables as sv

class Genesis(Space):
    def __init__(self, position, layer, reference_position, color):
        super().__init__(position)
        self.empty = False
        self.layer = layer
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.reference_position = reference_position # Position were neuron reference exist in array
        self.soma = ct.neural_array[self.reference_position] # A reference to the parent soma body
        self.length = sv.GL
        self.head = 0
        self.genesis_array = np.zeros((self.length, 3), dtype=int)
        self.weight = sv.direction_bias[self.layer-1]
        self.growing = True
        self.color = [0.5, 0.2, 0.2]
        #self.color[0] = color[0] * 2 # Red tints axon

        # Inserts first segment in genesis growth
        self.genesis_array[self.head] = position

    def growth(self):
        #print("Out")
        #print(self.growing == True and self.head < len(self.genesis_array)-1)
        if self.growing == True and self.head < self.length-1:
            #print("In")
            #for n in range(10): print(random.choices([1,2,3,4,5,6], weights=self.weight))
            # Selects a direction for genesis growth
            growth_direction = sv.direction_matrix[random.choices([1,2,3,4,5,6], weights=self.weight)[0]-1][(random.getrandbits(3) % 9) + 1]

            self.head += 1

            self.genesis_array[self.head] = growth_direction + self.genesis_array[self.head-1]

