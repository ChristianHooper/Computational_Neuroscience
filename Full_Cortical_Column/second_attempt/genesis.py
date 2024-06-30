import numpy as np
import controller as ct
import random
from space import Space
import project_variables as sv

class Genesis(Space):
    def __init__(self, position, layer, reference_position, color):
        super().__init__(position)
        self.empty = False # Exists as matter
        self.layer = layer # Layer originates form
        self.x = position[0] # Soma x-position (First segment; x, y, z)
        self.y = position[1] # Soma y-position
        self.z = position[2] # Soma z-position
        self.reference_position = reference_position # Position were neuron reference exist in array
        self.soma = ct.neural_array[self.reference_position] # A reference to the parent soma body
        self.length = sv.GL # Max length
        self.head = 0 # Starting length
        # The position of each axonal/dendritic segment in the object
        self.genesis_array = np.zeros((self.length, 3), dtype=int)
        self.weight = sv.direction_bias[self.layer-1] # The directional bias the segment grows toward
        self.growing = True # If the object is extending or not
        self.color = color # Color of the render
        self.genesis_array[self.head] = position # Inserts first segment in genesis growth

    def growth(self): # Retracts of extends growth of object
        if self.growing == False and self.head > 1: # Retracts grows to define new growth path
            self.genesis_array[self.head] = [0, 0, 0]
            self.head -= 1
            if random.getrandbits(4) == 0: self.growing = True # Activate growth
        else: self.growing = True

        # Grows the object by one segment value and updates position
        if self.growing == True and self.head < self.length-1:
            # Selects a direction for genesis growth
            growth_direction = sv.direction_matrix[np.random.choice([0,1,2,3,4,5], p=self.weight)][int(9 * random.random())]

            self.head += 1 # Advances one position
            # Create position for the next growth
            self.genesis_array[self.head] = growth_direction + self.genesis_array[self.head-1]

            if random.getrandbits(5) == 0: self.growing = False # If growth switch to retracting

