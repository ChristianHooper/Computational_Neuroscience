import numpy as np
import project_variables as sv
import random 
#print("HOLD :", sv.normalize(16, 128, 0))


array = [0.6, 0.6, 1.0]

solution = [a * (25 * 0.01) + 0.3 for a in array]

#print(solution)

test_arr = np.zeros((20, 3), dtype=int)

#print(test_arr)
one = np.zeros(1000000)
two = np.zeros(1000000)

sv.set_time()
for n in range(len(one)):
    one[n] = (random.getrandbits(3) % 6) + 1
sv.get_time()

sv.set_time()
for n in range(len(two)):
    one[n] = int(6 * random.random())
sv.get_time()

print(sv.direction_matrix.shape)