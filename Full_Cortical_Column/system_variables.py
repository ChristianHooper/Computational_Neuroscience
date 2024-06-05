# Wave frequencies for neural oscillations.
wave_frequencies = {'delta':(.5,4),
                    'theta': (4, 8),
                    'alpha': (8, 12),
                    'beta': (12, 30),
                    'gamma': (30, 100)}

# Y-axis layer depth variables, modeled after the occipital cortex. (micro-meters)
layers = {'width': (30, 50),
        'i':(0, 150),
        'ii': (150, 300),
        'iii':(300, 600),
        'iv': (600, 1000),
        'v':  (1000, 1400),
        'vi': (1400, 1600)}