import numpy as np
from space import Space

class Soma(Space):
    def __init__(self, position, layer):
        super().__init__(position)
        self.empty = False
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.layer = layer


    def __lt__(self, other):
        return self.y < other.y
