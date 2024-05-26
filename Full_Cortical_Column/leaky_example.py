import numpy as np
import matplotlib.pyplot as plt

# Parameters
tmax = 10  # Max time
dt = 0.1  # Time step
tau = 1  # Time constant (rate of decay)

# Input current: sparse spikes
time_steps = int(tmax / dt) # 100 steps

I = np.zeros(time_steps) # 100 zero array

spike_times = [2, 4, 8]  # Times at which input spikes occur


for spike_time in spike_times: # Marks index 10, 40, and 80 with a 1; all others are 0.
    I[int(spike_time / dt)] = 1


# Initialize membrane potential
V = np.zeros(time_steps) # Array of 100 zeros.


for t in range(1, time_steps): # Goes over all indices in array.
    V[t] = V[t-1] + dt / tau * (-V[t-1] + I[t]) # (index-1 + .1 / 1 * (-index-1 + 0||1)) If 1 at I[t] spike

# Plotting
plt.plot(np.arange(0, tmax, dt), V, label='Membrane Potential')
plt.plot(np.arange(0, tmax, dt), I, label='Input Current', linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Membrane Potential / Input Current')
plt.legend()
plt.show()