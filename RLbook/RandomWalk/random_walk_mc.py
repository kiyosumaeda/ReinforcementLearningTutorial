import random
import math
import numpy as np

alpha = 0.04
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
	returns = [[0 for k in range(1)] for l in range(7)]
	for i in range(episodes):
		s = 3
		state_list = []
		state_list.append(s)
		g = 0
		while s>= 1 and s<=5:
			action_index = random.randint(0, 1)
			action = a[action_index]
			new_state = s + action
			state_list.append(new_state)
			if new_state == 6:
				g = 1
			s = new_state
		for m in range(len(state_list)):
			if (state_list[m] != 6):
				v[state_list[m]] = v[state_list[m]] + alpha*(g-v[state_list[m]])
		rms[i] += (math.sqrt(np.sum((v-tv)**2)/5))
		# print(rms[i])
		# print(v)

with open("rms_mc_0_04.txt", "wt") as f:
	for e in rms:
		f.write(str(e)+'\n')
