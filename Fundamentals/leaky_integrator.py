import numpy as np
import matplotlib.pyplot as plt

tmax = 10; # Max time
dt = .1;  # Time step
tau = .1 # Rate of decay

X = np.zeros(tmax*int(1/dt)) # Total number of time steps. (Default 10)
a = np.array ([1, 2, 8])/dt # Create an array of 3 values divided by the time step.
X[a.astype(int)] = 1 # Indices of scalar array become 1.

x = np.array([0]) # One index, one row
for t in range(0, tmax*int(1/dt)): # Number of total steps.
    print(f'{x[t]}+{dt}*({-1/tau*x[t]})+{X[t]}) = {x[t]+dt*(-1/tau*x[t])+X[t]}') # Prints equation and product as each slice of time.
    x = np.append(x, x[t]+dt*(-1/tau*x[t])+X[t]) # Append new value in array, a scalar array defines spikes, tau sloped decay. (1.0+0.1*(-1.0)+0.0) = 0.9)

# Plot-data
plt.plot(x)
plt.xlabel('t in units of dt')
plt.show()
