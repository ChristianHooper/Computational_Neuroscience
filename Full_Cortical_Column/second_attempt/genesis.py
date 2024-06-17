import numpy as np


class Genesis(Space):
    def __init__(self, position):
        super().__init__(position)
        self.empty = False