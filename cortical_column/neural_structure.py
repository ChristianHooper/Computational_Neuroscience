import random

class Neuron:
    def __init__(self, x, y, z, number, set_fire):

        self.x = x # X position
        self.y = y # Y position
        self.z = z # Z position
        self.position = (x, y, z) # Functions as the position within the column.
        self.generation_id = number # When the neuron was generated.
        self.fire = set_fire
        self.membrane_potential = -70 # Resting potential of the cell to fire mV.
        self.resting_potential = -70
        self.axon_power = 3 # mV change in neuron when signal is received.
        self.dendrite_power = 2 # mV change in neuron when signal is received.
        self.neural_memory = 0
        self.history = 0


        # A part of the neuron. 
        self.outgoing_dendrites = [] # Incoming signals
        self.outgoing_axon = [] # Outgoing signals

    def action_potential(self):
        if self.membrane_potential >= -60: 
            membrane_potential = 40
            return True
    
    def add_dendrite(self, Neuron):
        self.outgoing_dendrites.append(Neuron)

    def add_axon(self, Neuron):
        self.outgoing_axon.append(Neuron)


class Cortical_Column:
    def __init__(self):
        self.neurons = []



    def add_neuron(self, x, y, z):
        neuron = Neuron(x, y, z, len(self.neurons), neural_genesis())
        self.neurons.append(neuron)


# //// Static Functions ///////////////////////////////////////////////////////////////
def neural_genesis(): # Starting odd for active neural structure. 
    if random.randint(1, 2) == 1: return True
    else: return False
    
