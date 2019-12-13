import random
import numpy as np

k = 10
total_step = 1000
episode = 2000
epsilon = 0
total_reward = [0 for i in range(total_step)]

# reward_list = [random.uniform(-3.0, 3.0) for i in range(k)]

for j in range(episode):
	reward_list = np.random.normal(0, 1, size=k)
	q = np.zeros(k)
	step_count = np.zeros(k)
	# print(reward_list)
	for i in range(total_step):
		random_value = random.random()
		if random_value<epsilon:
			a = random.randint(0, 9)
		else:
			a = np.argmax(q)
		# r = reward_list[a]
		reward_normal = np.random.normal(reward_list[a], 1, size=1000)
		r = reward_normal[random.randint(0, 999)]
		step_count[a] += 1
		q[a] = q[a]+(r-q[a])/step_count[a]
		total_reward[i] += r
		# average_reward = total_reward/step_count
		# print("step: ", step_count, " selected action: ", a, " average reward: ", average_reward)
	print("finished ", j, " step")

with open("reward3.txt", "wt") as f:
	for reward in total_reward:
		f.write(str(reward)+'\n')

for i in range(total_step):
	print("mean reward: ", total_reward[i]/episode)
