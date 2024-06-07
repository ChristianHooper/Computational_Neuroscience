# Wave frequencies for neural oscillations.
wave_frequencies = {'delta':(.5,4),
                    'theta': (4, 8),
                    'alpha': (8, 12),
                    'beta': (12, 30),
                    'gamma': (30, 100)}

# Y-axis layer depth variables, modeled after the occipital cortex. (micro-meters)
layers = {'width': (50),
        'i':(0, 150),
        'ii': (150, 300),
        'iii':(300, 600),
        'iv': (600, 1000),
        'v':  (1000, 1400),
        'vi': (1400, 1600)}
# Multiplicative layer weight bias i-iv (adds up to one, can do integers)
layer_bias = [0.05, 0.10, 0.2, 0.3, 0.2, 0.15]

# Neural types and their multiplicative bias weighting for generation selection
neural_type = {'i': [['interneurons'], [1]],
        'ii': [['stellate', 'small_pyramidal'], [1, 3]],
        'iii': [['pyramidal', 'interneurons'], [4, 1]],
        'iv': [['stellate', 'granule'], [1, 2]],
        'v': [['large_pyramidal', 'martinotti'], [3, 1]],
        'vi': [['fusiform', 'pyramidal', 'interneurons'], [2, 3, 1]]
        }

base_colors = {'i': (.60, .60, .60),
        'ii': (.60, .60, .90),
        'iii':(.60, .90, .60),
        'iv': (.60, .90, .90),
        'v':  (.90, .60, .60),
        'vi': (.90, .60, .90)
        }

total_neurons = 512

morpho_space = (layers['width'],layers['width'], layers['vi'][1]) # X, Y & Z morphological dimensions

def normalization(value, min=0, max=1):
        return (2 * ((value - min)/(max - min)) - 1)