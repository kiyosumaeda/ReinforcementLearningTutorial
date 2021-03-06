import random
import math
import numpy as np
import matplotlib.pyplot as plt

alpha = 0.05
tv = np.arange(0, 1.1, 1/6)
tv[6] = 0
a = [-1, 1]

gamma = 1
episodes = 100
rms = [0 for i in range(episodes)]
run = 100
for j in range(run):
	print("run: ", j)
	v = np.full(7, 0.5)
	v[0] = 0
	v[6] = 0
	for i in range(episodes):
		s = 3
		while s>=1 and s<=5:
			action_index = random.randint(0, 1);
			action = a[action_index]
			new_state = s + action
			reward = 0
			if new_state == 6:
				reward = 1
			v[s] = v[s] + alpha*(reward + gamma*v[new_state] - v[s])
			s = new_state
		rms[i] += (math.sqrt(np.sum((v-tv)**2)/5))

# print(rms)

with open("rms_0_05.txt", "wt") as f:
	for e in rms:
		f.write(str(e)+'\n')
