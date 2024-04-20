from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective

import numpy as np
import pygame as py
import math
import random
from voxel_class import Voxel
from voxel_render import *
#import voxel_render


# Data for the graph
base_graph = 20 # Width, length, and height in voxels. 
resolution = base_graph**3 # How many voxel square total the graph is made from.
color = [.5, .5, 1]
voxel_array = np.empty((base_graph, base_graph, base_graph), dtype=object)
render_stack = set()

# Intializes Voxel Graph 
for z in range(base_graph):
    for y in range(base_graph):
        for x in range(base_graph):
            voxel_array[x, y, z] = Voxel(x, y, z, random.randint(0, 6), color, base_graph)
            print(voxel_array[x, y, z])
            if voxel_array[x, y, z].render == 1:
                render_stack.add((x, y, z))
print(voxel_array)





def init(light_position):
    glEnable(GL_LIGHTING)  # Enable lighting
    glEnable(GL_LIGHT0)    # Enable light #0

    # Set light parameters
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (.2, .2, .2, 1))  # Color of light (White)
    #glLightfv(GL_LIGHT0, GL_SPECULAR, (0.2, 0.2, 0.2, 1))  # White specular light
    glLightfv(GL_LIGHT0, GL_AMBIENT, (.5, .5, .5, 1))  # Soft ambient light
    glEnable(GL_DEPTH_TEST)  # Enable depth testing
    
    
    glEnable(GL_COLOR_MATERIAL)  # Enable color material
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)  # Link glColor3fv to ambient and diffuse material properties
    glShadeModel(GL_SMOOTH) 


def draw_voxel(x, y, z):
    # Define vertice location in world space
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
    
    # Defines single vertices quads render from. (Front, Left, Top, Right, Back, Bottom)
    faces = (
    (0, 1, 2, 3), # Front face
    (3, 7, 6, 2), # Left face
    (2, 6, 5, 1), # Top Face
    (1, 0, 4, 5), # Right face
    (5, 6, 7, 4), # Back face
    (4, 7, 3, 0)  # Bottom face
    )
    
    normals = [
    (0, 0, 1),  # Front face
    (0, 0, -1), # Back face
    (1, 0, 0),  # Right faces
    (-1, 0, 0), # Left face
    (0, 1, 0),  # Bottom face
    (0, -1, 0)  # Top face
    ]

    whole_color = (0.8, 0.8, 1)
    

    # Set material properties
    #glMaterialfv(GL_FRONT, GL_DIFFUSE, (.5, .5, 1, 1))  # Diffuse color
    #glMaterialfv(GL_FRONT, GL_SPECULAR, (.1, .1, .1, 1))       # Specular color
    #glMaterialfv(GL_FRONT, GL_SHININESS,10)                 # Adjust shininess for sharper or softer highlights
    #glMaterialfv(GL_FRONT, GL_AMBIENT, (.4, .4, .4, 1))  # Soft ambient light
    
    
    glBegin(GL_QUADS) # Draws quads from the vertices 
    for i, face in enumerate(faces):
        glColor3fv(whole_color)  # Now affects material properties for lighting
        glNormal3fv(normals[i])  # Set normal for each face
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    py.init()
    display = (800, 800)
    py.display.set_mode(display, DOUBLEBUF|OPENGL)
    light_position = [0, 0, base_graph**4, 1] # [R, G, B, directional/orthographic]
    init(light_position) # Enable lighting
    
    # FOV, display distortion, near clipping, far clipping.
    #gluPerspective(100, (display[0]/display[1]), 0.1, 256.0)
    
    # Set up orthographic projection
    aspect_ratio = display[0] / display[1]
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # (Left, Right, Bottom, Top, zNear, zFar)
    glOrtho(-base_graph * aspect_ratio, base_graph * aspect_ratio, -base_graph, base_graph, -base_graph*2, base_graph**2)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Moves voxel in relration to the camera. 
    glTranslatef(0, -base_graph//10, -(base_graph)) # Centers voxels
    glRotatef(45, 1, 0, 0)  # Rotate around x-axis to look downwards
    glRotatef(45, 0, 0, 1)  # Rotate around z-axis to view from a corner 
    
    # Set the object's color
    #glColor3fv((1,0,0))
    
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)

        glRotatef(0, 0, 0, 90)  # Optional: Rotate the voxel for better visualization
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Draw the voxel at position (0, 0, 0)
        #draw_voxel(0, 0, 0)
        print("Render Start.")
        for v in render_stack:
            render_voxel(voxel_array[v[0], v[1], v[2]])
        render_stack.clear()

        for x in range(base_graph):
            for y in range(base_graph):
                for z in range(base_graph):
                    v = voxel_array[x, y, z]
                    v.render = random.randint(0, 2)
                    if v.render == 1:
                        render_stack.add((x, y, z))
                
        py.display.flip()
        py.time.wait(200)



# Functions
def get_time(): return py.time.get_ticks()



if __name__ == "__main__":
    main()
