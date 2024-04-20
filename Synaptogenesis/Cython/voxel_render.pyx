# cython: language_level=3
from cpython cimport array
import array
import numpy as np
cimport numpy as np
from voxel_class import Voxel
# Define no deprecated API before including NumPy headers
cdef extern from "numpy/arrayobject.h":
    pass

np.import_array()  # This must be called to complete initialization

# Open GL imports
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective





# faces[i*4 + j]
cdef int faces[24]
faces = [
    0, 1, 2, 3, # Front face
    3, 7, 6, 2, # Left face
    2, 6, 5, 1, # Top Face
    1, 0, 4, 5, # Right face
    5, 6, 7, 4, # Back face
    4, 7, 3, 0 # Bottom face
    ]

cdef int normals[18] 
normals = [
    0, 0, 1,  # Front face
    0, 0, -1,   # Back face
    1, 0, 0,   # Right faces
    -1, 0, 0,  # Left face
    0, 1, 0,  # Bottom face
    0, -1, 0    # Top face
    ]




'''
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
'''

cpdef render_voxel(voxel):
    glMaterialfv(GL_FRONT, GL_SPECULAR, (.1, .1, .1, 1))    # Specular color
    #glMaterialfv(GL_FRONT, GL_SHININESS,10)                 # Adjust shininess for sharper or softer highlights
    
    glBegin(GL_QUADS) # Draws quads from the vertices 
    for i in range(6):
        glColor3fv(voxel.color)  # Now affects material properties for lighting
        glNormal3fv(normals[i*3: i*3+3: 1]) # Sets the normals for each face
        for vertex in face[i*4: i*4+4: 1]:
            glVertex3fv(voxel.vertices[vertex])
    glEnd()

    '''
    REMAKE RENDERING LOOP
    
    glBegin(GL_QUADS) # Draws quads from the vertices 
    for i, face in enumerate(faces): #  index, item, list 
        glColor3fv(voxel.color)  # Now affects material properties for lighting
        glNormal3fv(normals[i])  # Set normal for each face
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()



    glBegin(GL_QUADS) # Draws quads from the vertices 
    for i, face in enumerate(faces):
        glColor3fv(whole_color)  # Now affects material properties for lighting
        glNormal3fv(normals[i])  # Set normal for each face
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()
    '''