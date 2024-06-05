import random
import numpy as np
import system_variables as sv
from neuron import Neuron


# Populates all possible position for cortical column
neural_array = np.empty(sv.morpho_space, dtype=Neuron)

position_guide = lambda axis_length: random.randint(0, axis_length-1)

position_array = np.empty([3]) # Holds the position of all neurons

for n in range(sv.total_neurons):
    
    position = np.array([ # Sets the posion to be pasted of to neuron
        position_guide(sv.layers['width']),  # Random X-axis position
        position_guide(sv.layers['width']),  # Random Y-axis position
        position_guide(sv.layers['iv'][1])]) # Random Z-axis position

    position_array[n] = [position]

    

    neural_array[position[0], position[1], position[2]] = Neuron(position, n)



print(position_array)