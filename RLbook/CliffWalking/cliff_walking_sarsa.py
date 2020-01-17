import random
import numpy as np

alpha = 0.1
epsion = 0.1
gamma = 1.0

actions = [[0,1], [1,0], [0,-1], [-1,0]]
width = 12
height = 4

sum_reward_list = [0 for i in range(500)]
runs = 100
episodes = 500
for j in range(runs):
	q = np.zeros((12, 4, 4))
	print("run: ", j)
	for i in range(episodes):
		pos_x = 0
		pos_y = 0
		sum_reward = 0
		# print("episode: ", i)
		while (pos_y>0 or pos_x==0):
			random_value = random.random()
			action_index = random.randint(0, 3)
			if random_value>=epsion:
				action_index = np.argmax(q[pos_x][pos_y])
			action = actions[action_index]
			new_pos_x = pos_x + action[0]
			new_pos_y = pos_y + action[1]
			reward = -1
			if new_pos_y==0 and new_pos_x==11:
				reward = -1
				print("goal!!!")
			elif new_pos_y == 0 and new_pos_x>=1:
				reward = -100
				print("you fall cliff...")
			
			if new_pos_x>11:
				new_pos_x = 11
			elif new_pos_x<0:
				new_pos_x = 0
	
			if new_pos_y>3:
				new_pos_y = 3
			elif new_pos_y<0:
				new_pos_y = 0
	
			q[pos_x][pos_y][action_index] = q[pos_x][pos_y][action_index] + alpha*(reward + gamma*np.max(q[new_pos_x][new_pos_y]) - q[pos_x][pos_y][action_index])
			pos_x = new_pos_x
			pos_y = new_pos_y
			# print("x: ", pos_x, ", y: ", pos_y)
			# print(q[0])
			sum_reward += reward
		# print(sum_reward)
		sum_reward_list[i] += sum_reward/100

print(sum_reward_list)

with open("cliff_q.txt", "wt") as f:
	for r in sum_reward_list:
		f.write(str(r)+'\n')
