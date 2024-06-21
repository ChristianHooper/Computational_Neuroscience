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
    one[n] = int(random.getrandbits(6)/7 % 9)+1 # Slightly bias to one
sv.get_time()

sv.set_time()
for n in range(len(two)):
    one[n] = int(9 * random.random())+1
sv.get_time()

# print(sv.direction_matrix.shape)

counted = {
    0: [0],
    1: [0],
    2: [0],
    3: [0],
    4: [0],
    5: [0],
    6: [0],
    7: [0],
    8: [0],
    9: [0],
    10:[0]
}

for n in range(10000):
    x = int(9 * random.random())+1
    counted[x][0] = counted[x][0]+1

print(counted)
