import numpy as np
import project_variables as sv
from space import Space

'''
Initializes cortical column using project variables
'''

morpho_space = np.empty(sv.MD, dtype=object) # Morphological Space represents total space in column and the column objects

sv.set_time() # Sets start of morphological space initialization
# Places Space object within the entire morphological space
# Efficiency doesn't matter as it's run once to initialize cortical column
for index, _ in np.ndenumerate(morpho_space):
    morpho_space[index] = Space(index)

print(f"Morphological Space Initialized: {morpho_space.shape}")
sv.get_time() # Print time morpho-space initialization took


 # Put all neurons in a 2-d 6 row numpy array, each with their own column (START HERE) Space object, neuron connection??