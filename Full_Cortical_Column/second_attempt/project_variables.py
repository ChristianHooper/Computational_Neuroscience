import numpy as np
from space import Space

WIDTH = 50 # Define the x-axis in micro-meters
LENGTH = 50 # Define the y-axis in micro-meters
DEPTH = 1500 # Define the z-axis in micro-meters

LP = np.array([10, 15, 15, 25, 15, 20]) # Layer Percentage out of 100 that defines layer size i-vi

LD = np.array(list(int((sum(LP[:n+1])/sum(LP)) * DEPTH) for n in range(len(LP)))) # Layer Division sets the upper bounds for each layer (Lower < Higher)


# Y-axis layer depth variables, modeled after the occipital cortex. (micro-meters)
layers = {'width': WIDTH, 'length': LENGTH,
        'i':(0, LD[0]),
        'ii': (LD[0], LD[1]),
        'iii':(LD[1], LD[2]),
        'iv': (LD[2], LD[3]),
        'v':  (LD[3], LD[4]),
        'vi': (LD[4], LD[5])}

print(f"Layers Information: {layers}") # Prints dimension data about the cortical column



# Sets X, Y & Z morphological dimensions
# Extends by one so that zero is not counted as a possible habitable space
MD = (layers['width']+1, layers['length']+1, layers['vi'][1]+1)




# Not adding Space objects to array, adds a None (START HERE)
# Represents total space in column and the column objects
morphological_space = np.empty(MD, dtype=Space)

print(morphological_space.shape)

print(morphological_space)









# Wave frequencies for neural oscillations.
wave_frequencies = {'delta':(1,4),
                    'theta': (4, 8),
                    'alpha': (8, 12),
                    'beta': (12, 30),
                    'gamma': (30, 100)}
