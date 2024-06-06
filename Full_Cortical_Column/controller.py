import random
import numpy as np
import system_variables as sv
from space import Space
from neuron import Neuron
from collections import OrderedDict
#from itertools import chain



# Populates all possible position for cortical column
morphological_array = np.empty(sv.morpho_space, dtype=Space)

# Places Space object within the entire morphological space
# Efficiency doesn't matter as it's run once to initialize cortical column
for index, _ in np.ndenumerate(morphological_array):
    morphological_array[index] = Space

# Generates a random value between 0 and a given length minus one
position_guide = lambda axis_start, axis_length: random.randint(axis_start, axis_length-1)

# Holds the position of all neurons as keys
position_dictionary = {}

def initialize():
    for n in range(sv.total_neurons):

        # Gets a random layer key to define nerons layer location from i-iv
        base_layers = list(sv.layers.keys()) # Converts keys to a list for selection
        
        # Pairs elements in a tuple and the multiplies them together
        # pre_layer = list(chain.from_iterable([s] * n for s, n in zip(base_layers[1:7], sv.layer_bias)))
        
        layer = random.choices(base_layers[1:7], weights=sv.layer_bias)[0]
    


        position = np.array([ # Sets the posion to be pasted of to neuron
        position_guide(sv.layers['i'][0], sv.layers['width']),  # Random X-axis 
        position_guide(sv.layers['i'][0], sv.layers['width']),  # Random Y-axis 
        position_guide(sv.layers[layer][0], sv.layers[layer][1])   # Random Z-axis 
        ])



        id = (position[0], position[1], position[2]) # Set dictionary key for neuron 

        neuron = Neuron(position, id, n, layer) # Initializes current neuron

        # Small dictionary of all neurons
        position_dictionary[id] = neuron

        # Large array of all neurons in the morphospace positions, and empty spaces
        morphological_array[position[0], position[1], position[2]] = neuron

    # Sorts neurons based upon their y-depth for proper color rendering
    # position_dictionary = OrderedDict(sorted(position_dictionary.items(), key=position_dictionary.values.y))

    print("[Controller Initialized]")

if __name__ == "__main__":
    initialize()

    #print(morphological_array)
    #print(position_dictionary)

