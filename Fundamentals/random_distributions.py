import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.random.rand(1000)
n, bias = np.histogram(x)
plt.bar(bias[:-1]+0.05, n/1000, 0.1)
plt.xlabel('x'), plt.ylabel('P(x)')