"""
Created on Wed Apr 22 15:21:11 2015

Code to compute spike-triggered average.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def compute_sta(stim, rho, num_timesteps):
    """Compute the spike-triggered average from a stimulus and spike-train.

    Args:
        stim: stimulus time-series
        rho: spike-train time-series
        num_timesteps: how many timesteps to use in STA

    Returns:
        spike-triggered average for num_timesteps timesteps before spike"""

    sta = np.zeros((num_timesteps,))

    # This command finds the indices of all of the spikes that occur
    # after 300 ms into the recording.
    spike_times = rho[num_timesteps:].nonzero()[0] + num_timesteps
    print("Spikes: ", len(spike_times))
    # Fill in this value. Note that you should not count spikes that occur
    # before 300 ms into the recording.
    num_spikes = len(spike_times)
    # Compute the spike-triggered average of the spikes found.
    # To do this, compute the average of all of the vectors
    # starting 300 ms (exclusive) before a spike and ending at the time of
    # the event (inclusive). Each of these vectors defines a list of
    # samples that is contained within a window of 300 ms before each
    # spike. The average of these vectors should be completed in an
    # element-wise manner.
    #
    # Your code goes here.

    # Sections out every spike and creates an array of lists that looks at the voltage data 300ms prior to response
    sta_glom = [stim[i:i-num_timesteps: -1] for i in spike_times]

    # Converts the array into a list of variables at the same time interval based upon each stimulus (Transforms cols to rows)
    sta_col_glom = [[sta_glom[i][u] for i in range(len(sta_glom))] for u in range(num_timesteps)]

    # Averages all the voltages values at each timer interval across all spikes to create a spike-time average
    sta = [np.sum(sta_col_glom[i])/len(spike_times) for i in range(len(sta_col_glom))]





    return sta