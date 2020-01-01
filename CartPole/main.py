import gym

from CartPoleAgent import Agent


ENV = 'CartPole-v0'
STEPS = 200
EPISODES = 2000

episode_list = []

env = gym.make(ENV)
states_num = env.observation_space.shape[0]
actions_num = env.action_space.n
agent = Agent(states_num, actions_num)

for i in range(EPISODES):
	observation = env.reset()
	for j in range(STEPS):
		env.render()
		action = agent.take_action(observation, i)
		next_observation, r, done, info = env.step(action)

		if done:
			reward = -1 if j < 195 else 1
		else:
			reward = 0

		agent.update(observation, action, reward, next_observation)

		observation = next_observation

		if done:
			print(i, " episode finished, ", j+1, " time step")
			episode_list.append(j+1)
			break

with open("step3.txt", "wt") as f:
	for episode in episode_list:
		f.write(str(episode)+'\n')
