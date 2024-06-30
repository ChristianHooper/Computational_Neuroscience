import random
import numpy as np
from space import Space
from genesis import Genesis

class Soma(Space):
    def __init__(self, position, layer, color, reference_position, type_list):
        super().__init__(position)
        self.empty = False
        self.position = position
        self.type = random.choices(type_list)[0] # Type pf neuron, layer dependent
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.layer = layer
        self.reference_position = reference_position # Position were neuron reference exist in array
        # Defines soma color based upon y-axis depth
        self.color = [channel * (self.y * 0.01) + 0.3 for channel in color]
        # Initializes axon on neuron
        self.axon = Genesis(position, layer, self.reference_position, [0.4, 0.2, 0.2])
        # Initializes dendrite on neuron
        self.dendrite = Genesis(position, layer, self.reference_position, [0.2, 0.2, 0.4])



    def __lt__(self, other): # Neurons are rendered based upon y-axis depth (Deep first-to-render)
        return self.y < other.y
