import pygame
import math

class Arrow():
    def __init__(self, window):
        self.window = window
        self.start_x = 75
        self.start_y = 75
        self.line_length = 50
        self.degree = 90
        

    def endpoint(self, angle):
        self.degree = angle

        x = self.start_x + self.line_length * math.cos(self.degree)
        y = self.start_y + self.line_length * math.sin(self.degree)
        return (x, y)

    def render(self, angle):
        pygame.draw.line(self.window, (0, 255, 0), (self.start_x, self.start_y), self.endpoint(angle), width=5)