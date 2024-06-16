import time
import numpy as np


'''
Variables in the document do not change, they drive the initialization and behavior of the cortical column.
'''

WIDTH = 50 # Define the x-axis in micro-meters
LENGTH = 50 # Define the y-axis in micro-meters
DEPTH = 1500 # Define the z-axis in micro-meters

start_time = 0.0
def set_time(): global start_time; print("\n| Time start"); start_time = time.perf_counter() # Sets timer when called
def get_time(): global start_time; print(f"| Time taken: {time.perf_counter() - start_time}\n") # Prints time since timer has been called

LP = np.array([10, 15, 10, 30, 15, 20]) # Layer Percentage out of 100 that defines layer size i-vi

LD = np.array(list(int((sum(LP[:n+1])/sum(LP)) * DEPTH) for n in range(len(LP)))) # Layer Division sets the upper bounds for each layer (Lower < Higher)


# Y-axis layer depth variables, modeled after the occipital cortex. (micro-meters)
layers = {'width': WIDTH, 'length': LENGTH,
        'i':(0, LD[0]),
        'ii': (LD[0], LD[1]),
        'iii':(LD[1], LD[2]),
        'iv': (LD[2], LD[3]),
        'v':  (LD[3], LD[4]),
        'vi': (LD[4], LD[5])}

print(f"Layer Information: {layers}") # Prints dimension data about the cortical column

# Sets X, Y & Z morphological dimensions
# Morphological Dimensions extends by one so that zero is not counted as a possible habitable space
MD = (layers['width']+1, layers['length']+1, layers['vi'][1]+1)










# Wave frequencies for neural oscillations.
wave_frequencies = {'delta':(1,4),
                    'theta': (4, 8),
                    'alpha': (8, 12),
                    'beta': (12, 30),
                    'gamma': (30, 100)}
