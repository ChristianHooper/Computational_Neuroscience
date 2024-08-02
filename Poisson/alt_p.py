import numpy as np
import matplotlib.pyplot as plt

# Parameters
rate = 100  # Firing rate in Hz
duration = 10  # Duration of the simulation in seconds
dt = 0.001  # Time step in seconds
total_time_steps = int(duration / dt)

# Generate Poisson spike train
np.random.seed(0)  # For reproducibility
p = rate * dt  # Probability of a spike in each time step
spikes = np.random.rand(total_time_steps) < p
spike_times = np.where(spikes)[0] * dt  # Convert to time in seconds

# Calculate interspike intervals (ISIs)
isis = np.diff(spike_times)

# Calculate coefficient of variation (CV)
mean_isi = np.mean(isis)
std_isi = np.std(isis)
cv_isi = std_isi / mean_isi

# Calculate Fano factor for different counting intervals
count_intervals = np.arange(0.001, 0.101, 0.001)  # From 1 ms to 100 ms
fano_factors = []

for interval in count_intervals:
    num_bins = int(duration / interval)
    spike_counts = np.histogram(spike_times, bins=num_bins, range=(0, duration))[0]
    mean_count = np.mean(spike_counts)
    variance_count = np.var(spike_counts)
    fano_factor = variance_count / mean_count if mean_count > 0 else np.nan
    fano_factors.append(fano_factor)

# Plot ISI histogram
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(isis, bins=30, edgecolor='k', alpha=0.7)
plt.xlabel('Interspike Interval (s)')
plt.ylabel('Frequency')
plt.title('Interspike Interval Histogram')

# Plot Fano factors
plt.subplot(1, 2, 2)
plt.plot(count_intervals * 1000, fano_factors, marker='o')  # Convert to ms
plt.xlabel('Counting Interval (ms)')
plt.ylabel('Fano Factor')
plt.title('Fano Factor vs. Counting Interval')
plt.grid(True)

plt.tight_layout()
plt.show()

# Print results
print("Mean ISI:", mean_isi)
print("Standard Deviation of ISIs:", std_isi)
print("Coefficient of Variation of ISIs:", cv_isi)