import time

dt = .001 # Hundredth of a second delta_time base, only has one step to deal with peak gamma wave.

start_time = time.time()

# Wave frequencies for neural oscillations.
wave_frequencies = {'delta':(.5,4),
                    'theta': (4, 8),
                    'alpha': (8, 12),
                    'beta': (12, 30),
                    'gamma': (30, 100)}

time.sleep(2.5)

current_time = time.time() - start_time



print(current_time)