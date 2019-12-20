import gym
import pandas as pd

env = gym.make('Breakout-v0')
for i_episode in range(20):
	observation = env.reset()
	for t in range(100):
		env.render()
		action = env.action_space.sample()
		# action = 3
		observation, reward, done, info = env.step(action)
		# print("action: ", action, ", observation: ", observation)
		if (i_episode==0 and t==0):
			for i in range(len(observation)):
				for j in range(len(observation[i])):
					print(observation[i][j])
		if done:
			print("done episode")
			break
env.close()
