# Example of numerical Intergration
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def xdot(x, t):
    return x

x0 = 1
dt = 0.1
t = np.arange(0, 3, dt)

xEuler = np.array([x0])
for step in t:
    xEuler = np.append(xEuler, xEuler[-1]+dt*xdot(xEuler[-1], step))

xODEint = np.squeeze(odeint(xdot, x0, t))

xAna = x0 * np.exp(t) # Analyitic solution

plt.plot(t, xEuler[:-1], 'r-'); plt.plot(t, xAna)
plt.xlabel('t'); plt.ylabel('xEuler, xAna')
plt.show()