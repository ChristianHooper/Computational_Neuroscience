import random
import numpy as np
import project_variables as sv
from space import Space
from soma import Soma


'''
Initializes cortical column using project variables & controls cortical processes.
'''

# Morphological Space represents total space in column and the column objects
morpho_space = np.empty(sv.MD, dtype=object)

# List of all generated neuron object independent of morphological space
neural_array = np.empty(sv.TN, dtype=object)


def initialize_cortical_column(): # Create the cortical column prior to runtime

    sv.set_time() # Sets start of morphological space initialization
    # Places Space object within the entire morphological space
    # Efficiency doesn't matter as it's run once to initialize cortical column
    for index, _ in np.ndenumerate(morpho_space):
        morpho_space[index] = Space(index)
    print(f"[Morphological Space Initialized: {morpho_space.shape}]")
    sv.get_time() # Print time morpho-space initialization took

    sv.set_time()
    for neuron in range(sv.TN): # Generates, place, and sorts neurons based upon y-depth
        duplicate = False
        while not duplicate: # Allows neural generation to re-run if a neuron spawn in a position that is already occupied

            # Put all neurons in a 2-d 6 row numpy array, each with their own column (START HERE) Space object, neuron connection??
            layer_selection = random.choices([1, 2, 3, 4, 5, 6], weights=sv.SW)[0] # Selects layer for neuron spawn

            # X, Y, and Z positions on morpho-space for neuron
            position = (random.randint(0, sv.WIDTH), random.randint(0, sv.WIDTH), random.randint(*sv.layers[layer_selection]))

            if morpho_space[*position].empty != False: # Generates neuron if neuron doesn't exist in current position

                soma = Soma(position, layer_selection, sv.color[layer_selection-1], neuron, sv.neuron_type[layer_selection])
                morpho_space[*position] = soma # Adds neuron to cortical column morpho-space
                neural_array[neuron] = morpho_space[*position] # Adds neuron reference to list of all neuron for quick calling, pass off to np.array
                break
            else:
                # print(f"[Duplicate Neuron Generated]")
                duplicate = True # If neuron spawn is same position, re-runs generation
            duplicate = False
    neural_array.sort()
    print(f"[Neurons Initialized]")
    sv.get_time()

def cortical_functions():
    for neuron in neural_array: # Call each existing neuron
        neuron.axon.growth() # Grows axonal segment by one
        neuron.dendrite.growth() # Grows axonal segment by one

if __name__ == "__main__":
    initialize_cortical_column()