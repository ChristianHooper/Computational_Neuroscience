import numpy as np
from space import Space

class Soma(Space):
    def __init__(self, position, layer, color):
        super().__init__(position)
        self.empty = False
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.layer = layer
        # Defines soma color based upon y-axis depth
        self.color = [channel * (self.y * 0.01) + 0.3 for channel in color]


    def __lt__(self, other): # Neurons are rendered based upon y-axis depth (Deep first-to-render)
        return self.y < other.y
