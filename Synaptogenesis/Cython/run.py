from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective

import SynaptogenesisCy
import numpy as np
import pygame as py
import math
import random



def draw_voxel(x, y, z):
    # Define vertices of the voxel
    vertices = (
        (1 + x, -1 + y, -1 + z),
        (1 + x, 1 + y, -1 + z),
        (-1 + x, 1 + y, -1 + z),
        (-1 + x, -1 + y, -1 + z),
        (1 + x, -1 + y, 1 + z),
        (1 + x, 1 + y, 1 + z),
        (-1 + x, -1 + y, 1 + z),
        (-1 + x, 1 + y, 1 + z)
    )
    
    # Define the edges connecting the vertices
    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        (5, 7)
    )

    # Draw the edges
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    py.init()
    display = (800, 600)
    py.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    # Set perspective
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    
    # Move back so we can see the voxel
    glTranslatef(0.0, 0.0, -10)
    
    # Set the object's color
    glColor3fv((1,0,0))
    
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
        
        glRotatef(.1, 1, 1, 1)  # Optional: Rotate the voxel for better visualization
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        # Draw the voxel at position (0, 0, 0)
        draw_voxel(0, 0, 0)
        
        py.display.flip()
        py.time.wait(10)


# Functions
def get_time(): return py.time.get_ticks()


SynaptogenesisCy.Testing()

if __name__ == "__main__":
    main()
