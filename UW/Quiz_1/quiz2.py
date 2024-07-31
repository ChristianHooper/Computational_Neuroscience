"""
Created on Wed Apr 22 15:15:16 2015

Quiz 2 code.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

import pickle

from compute_sta import compute_sta


FILENAME = 'c1p8.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

stim = data['stim'] # Stimulus data, 600k points
rho = data['rho'] # Spike times 600k points, 53k spikes


print("RHO:", np.sum(rho))


# Fill in these values
sampling_period = 2 # Time interval for data in ms
num_timesteps = 150 # Number of steps in data display

sta = compute_sta(stim, rho, num_timesteps)

time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')

plt.show()