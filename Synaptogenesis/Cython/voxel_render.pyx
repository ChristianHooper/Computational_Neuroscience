# cython: language_level=3
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
from cpython cimport array
import array
import numpy as np
cimport numpy as np

# Define no deprecated API before including NumPy headers
cdef extern from "numpy/arrayobject.h":
    pass

np.import_array()

# Open GL imports
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective

cpdef render_voxel(voxel):
    
    cdef list faces
    faces = [
        0, 1, 2, 3, # Front face
        3, 7, 6, 2, # Left face
        2, 6, 5, 1, # Top Face
        1, 0, 4, 5, # Right face
        5, 6, 7, 4, # Back face
        4, 7, 3, 0 # Bottom face
        ]


    cdef list normals
    normals = [
        0, 0, 1,  # Front face
        0, 0, -1, # Back face
        1, 0, 0,  # Right faces
        -1, 0, 0, # Left face
        0, 1, 0,  # Bottom face
        0, -1, 0  # Top face
        ]

    glMaterialfv(GL_FRONT, GL_SPECULAR, (.1, .1, .1, 1)) # Specular color
    #glMaterialfv(GL_FRONT, GL_SHININESS,10)

    glBegin(GL_QUADS)
    for i in range(6):
        glColor3fv(voxel.color)
        glNormal3fv(normals[i*3: i*3+3: 1])
        for j in faces[i*4: i*4+4: 1]:
            glVertex3fv(voxel.vertex_data[j])
    glEnd()

    
