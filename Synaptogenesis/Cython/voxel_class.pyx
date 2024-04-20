# cython: language_level=3
from cpython cimport array
import array
import numpy as np
cimport numpy as np
# Define no deprecated API before including NumPy headers
cdef extern from "numpy/arrayobject.h":
    pass

np.import_array()  # This must be called to complete initialization




cdef class Voxel:
    cdef int _x, _y, _z # Voxel position for rendering.
    cdef int _render # If the voxel should render.
    cdef int base # If the voxel should render.
    cdef np.ndarray _color_array# Initializes np color array.
    cdef float[:] color_view # Initializes memory view for np array.

    def __init__(self, int x, int y, int z, int render, list color, int base):
        self._x = x
        self._y = y
        self._z = z
        self.base = base
        self._render = render
        self._color_array = np.array(color, dtype = np.float32) # Color values (ndim=One-dimension)
        self.vertices
        calculate_vertices()
        self.ID = calculate_id()

     # Provides direct, mutable access to the np array (Getter & Setter)
    @property # Returns a memory view of the np array, refrencing it instead of copying it. 
    def color(self): return self._color_array[:]

    @property # X-axis getter
    def x(self): return self._x
    @x.setter # X-axis setter
    def x(self, new_x): 
        self._x = new_x
        calculate_vertices()

    @property # Y-axis getter
    def y(self): return self._y
    @y.setter # Y-axis setter
    def y(self, new_y): 
        self._y = new_y
        calculate_vertices()

    @property # Z-axis getter
    def z(self): return self._z
    @z.setter # Z-axis setter
    def z(self, new_z): 
        self._z = new_z
        calculate_vertices()

    @property # Gets render state
    def render(self): return self._render
    @render.setter # Sets render (1=render | 0=non-render)
    def render(self, if_render): self._render = if_render

    cpdef calculate_vertices():   # Define vertice location in world space
        self.vertices = (
        (1 + self._x, -1 + self._y, 1 + self._z),   # 0 Front Bottom Right
        (1 + self._x, 1 + self._y, 1 + self._z),    # 1 Front Top Right
        (-1 + self._x, 1 + self._y, 1 + self._z),   # 2 Front Top Left
        (-1 + self._x, -1 + self._y, 1 + self._z),  # 3 Front Bottom Left
        
        (1 + self._x, -1 + self._y, -1 + self._z),  # 4 Back Bottom Right  
        (1 + self._x, 1 + self._y, -1 + self._z),   # 5 Back Top Right     
        (-1 + self._x, 1 + self._y, -1 + self._z),  # 6 Back Top Left
        (-1 + self._x, -1 + self._y, -1 + self._z), # 7 Back Bottom Left
        )

    cpdef calculate_id(): # Intial ID calcuation holds the place at which the voxel was generated in relation to the other voxels.
        return [self._x, self._y, self._z]
        #(self._x + (self._y*self.base) + (self._z*self.base))
