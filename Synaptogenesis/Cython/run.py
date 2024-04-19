from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective

import SynaptogenesisCy
import numpy as np
import pygame as py
import math
import random

def init(light_position):
    glEnable(GL_LIGHTING)  # Enable lighting
    glEnable(GL_LIGHT0)    # Enable light #0

    # Set light parameters
    light_position = [1, 1, 1, 0]  # Positioned infinitely far away (directional light)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1))  # White diffuse light
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0.2, 0.2, 0.2, 1))  # White specular light
    glLightfv(GL_LIGHT0, GL_AMBIENT, (.6, .6, .6, 1))  # Soft ambient light
    glEnable(GL_DEPTH_TEST)  # Enable depth testing

def draw_voxel(x, y, z):

    # Define vertices of the voxel
    vertices = (
    (1 + x, -1 + y, 1 + z),   # 0 Front Bottom Right
    (1 + x, 1 + y, 1 + z),    # 1 Front Top Right
    (-1 + x, 1 + y, 1 + z),   # 2 Front Top Left
    (-1 + x, -1 + y, 1 + z),  # 3 Front Bottom Left
    

    (1 + x, -1 + y, -1 + z),  # 4 Back Bottom Right  
    (1 + x, 1 + y, -1 + z),   # 5 Back Top Right     
    (-1 + x, 1 + y, -1 + z),  # 6 Back Top Left
    (-1 + x, -1 + y, -1 + z), # 7 Back Bottom Left

    )
    
    # Define vertices quads render on.(Front, Left, Top, Right, Back, Bottom)
    faces = (
    (0, 1, 2, 3), # Front face
    (3, 7, 6, 2), # Left face
    (2, 6, 5, 1), # Top Face
    (1, 0, 4, 5), # Right face
    (5, 6, 7, 4), # Back face
    (4, 7, 3, 0)
    )
    
    normals = [
    (0, 0, -1),  # Front face
    (0, 0, 1),   # Back face
    (1, 0, 0),   # Right face
    (-1, 0, 0),  # Left face
    (0, -1, 0),  # Bottom face
    (0, 1, 0)    # Top face
    ]
    
    
    colors = [
        (1, 0, 0),  # Red
        (0, 1, 0),  # Green
        (0, 0, 1),  # Blue
        (1, 1, 0),  # Yellow
        (1, 0, 1),  # Magenta
        (0, 1, 1)   # Cyan
    ]
    

    # Set material properties
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.5, 0.5, 0.5, 1))  # Diffuse color
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.4, 0.4, 0.4, 1))       # Specular color
    glMaterialfv(GL_FRONT, GL_SHININESS, 50)                # Shininess
    
    '''NOT RENDERING properly, check faces'''
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor3fv(colors[i])  # Set color for each face
        glNormal3fv(normals[i])  # Set the normal for the current face
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    py.init()
    display = (800, 600)
    py.display.set_mode(display, DOUBLEBUF|OPENGL)
    light_position = [1, 1, 1, 0]
    init(light_position) # Enable lighting
    
    # FOV, display distortion, near clipping, far clipping.
    gluPerspective(75, (display[0]/display[1]), 0.1, 256.0)
    
    glTranslatef(0, -2.0, -10) # Moves voxel in relration to the camera. 
    
    # Set the object's color
    glColor3fv((1,0,0))
    
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)

        glRotatef(1, 1, 1, 1)  # Optional: Rotate the voxel for better visualization
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Draw the voxel at position (0, 0, 0)
        draw_voxel(0, 0, 0)
        
        py.display.flip()
        py.time.wait(10)



# Functions
def get_time(): return py.time.get_ticks()


SynaptogenesisCy.Testing()

if __name__ == "__main__":
    main()
