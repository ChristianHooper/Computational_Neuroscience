import numpy as np
import matplotlib.pyplot as plt

hertz = 100
dt = 0.1/hertz # Length of intervals
print(dt)
T = 10 # Total simulation time
r = 5 # Firing rate in spikes per second
p = r*dt # Probability of spike within interval (0.005%)



def time_correction(x): return x/1000

# Simulates spike train
spikes = np.random.rand(int(T/dt)) # 1000 random var within 0-1
spikes[spikes < p] = 1 # Sets spikes to 1
spikes[spikes < 1] = 0 # Set all others to 0

spike_times = np.where(spikes == 1)[0] # Spike times

# Summation and average on spike intervals
intervals = [time_correction(spike_times[i]-spike_times[i-1]) for i in range(len(spike_times))]; del intervals[0]
ISI = np.sum(intervals)/len(spike_times) # Interspike Interval
print(intervals)


# ISI standard deviation
variance = (np.sum((intervals[:]-ISI)**2))/len(intervals)
SD_ISI = np.sqrt(variance)



plt.plot(np.arange(T*1000), spikes)
plt.xlabel("Time(ms)")
plt.ylabel("Spikes")
plt.title("Poisson Neuron")

plt.show()


