import time
import numpy as np


'''
Variables in the document do not change, they drive the initialization and behavior of the cortical column.
Measured depth based upon layers in cortical column
'''

WIDTH = 50 # Define the x-axis in micro-meters
LENGTH = 50 # Define the y-axis in micro-meters
DEPTH = 1500 # Define the z-axis in micro-meters

render = True # If the column should render or not

TN = 256 # Total neurons initialized in cortical column
GL = 1024 # Genesis length, how long both axons and dendrites can be by default

LP = np.array([10, 15, 10, 30, 15, 20]) # Layer Percentage out of 100 that defines layer size i-vi

SW = np.array([0.05, 0.15, 0.10, 0.35, 0.15, 0.20]) # Spawn weight defines the bias for neuron layer spawning, index indicates layer

LD = np.array(list(int((sum(LP[:n+1])/sum(LP)) * DEPTH) for n in range(len(LP)))) # Layer Division sets the upper bounds for each layer (Lower < Higher)

start_time = 0.0
def set_time(): global start_time; print("\n| Time start"); start_time = time.perf_counter() # Sets timer when called
def get_time(): global start_time; print(f"| Time taken: {time.perf_counter() - start_time}\n") # Prints time since timer has been called

# Returns a normalized value of a input from a given range, -1 to 1 scale
def normalize(value, max=1, min=0):
        return (2 * ((value - min)/(max - min)) - 1)

# Returns a normalized value of a input from a given range, 0 to 1 scale
def normalize_zero(value, max=1, min=0):
        return ((value - min)/(max - min))

# Y-axis layer depth variables, modeled after the occipital cortex. (micro-meters)
layers = {'width': WIDTH,
        1: (0, LD[0]),
        2: (LD[0], LD[1]),
        3: (LD[1], LD[2]),
        4: (LD[2], LD[3]),
        5: (LD[3], LD[4]),
        6: (LD[4], LD[5]),
        'length': LENGTH
        }

color = np.array([ # Defines the color of neurons based upon their respective layer
        [0.5, 0.5, 0.5], # Layer One
        [0.5, 0.5, 1.0],
        [0.5, 1.0, 0.5],
        [0.5, 1.0, 1.0],
        [1.0, 0.5, 0.5],
        [1.0, 0.5, 1.0]]) # Layer Six

direction_matrix = np.array([
        [[-1,-1,1], [-1,0, 1], [-1,1, 1], # Descending z-axis
        [0, -1, 1], [0, 0, 1], [0, 1, 1],
        [1, -1, 1], [1, 0, 1], [1, 1, 1]],

        [[-1,-1,-1], [-1, 0,-1], [-1,1, -1], # Ascending z-axis
        [0, -1, -1], [0, 0, -1], [0, 1, -1],
        [1, -1, -1], [1, 0, -1], [1, 1, -1]],

        [[-1, 1,-1], [-1, 1, 0], [-1, 1, 1], # Ascending x-axis
        [-1, 0, -1], [-1, 0, 0], [-1, 0, 1],
        [-1,-1, -1], [-1, -1,0], [-1,-1, 1]],

        [[1, 1,-1], [1, 1, 0], [1, 1, 1], # Descending x-axis
        [1, 0, -1], [1, 0, 0], [1, 0, 1],
        [1,-1, -1], [1, -1,0], [1,-1, 1]],

        [[-1,-1,-1], [-1,-1, 0], [-1,-1,1], # Ascending y-axis
        [0, -1, -1], [0, -1, 0], [0,-1, 1],
        [1, -1, -1], [1, -1, 0], [1,-1, 1]],

        [[-1,-1,-1], [-1,-1, 0], [-1,-1, 1], # Descending y-axis
        [0, -1, -1], [0, -1, 0], [0, -1, 1],
        [1, -1, -1], [1, -1, 0], [1, -1, 1]],
])

direction_bias = [ # +Z, -Z, -X, +X, -Y, +Y
        [0.5, 0.1, 0.1, 0.1, 0.1, 0.1], # Layer One
        [0.5, 0.1, 0.1, 0.1, 0.1, 0.1], # Layer Two
        [0.5, 0.1, 0.1, 0.1, 0.1, 0.1], # Layer Three

        [0.3, 0.3, 0.1, 0.1, 0.1, 0.1], # Layer Four

        [0.1, 0.5, 0.1, 0.1, 0.1, 0.1], # Layer Five
        [0.1, 0.5, 0.1, 0.1, 0.1, 0.1]  # Layer Six
]

neuron_type = {0: [[None]],
        1: ['interneurons'],
        2: ['stellate', 'small_pyramidal'],
        3: ['pyramidal', 'interneurons'],
        4: ['stellate', 'granule'],
        5: ['large_pyramidal', 'martinotti'],
        6: ['fusiform', 'pyramidal', 'interneurons']
        }

print(f"Layer Information: {layers}") # Prints dimension data about the cortical column

# Sets X, Y & Z morphological dimensions
# Morphological Dimensions extends by one so that zero is not counted as a possible habitable space
MD = (layers['width']+1, layers['length']+1, layers[6][1]+1)

# Wave frequencies for neural oscillations.
wave_frequencies = {'delta':(1,4),
                    'theta': (4, 8),
                    'alpha': (8, 12),
                    'beta': (12, 30),
                    'gamma': (30, 100)}
