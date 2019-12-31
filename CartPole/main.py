import gym

from CartPoleAgent import Agent


ENV = 'CartPole-v0'
STEPS = 200
EPISODES = 1000

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
			if j < 200:
				reward = -1
			else:
				reward = 1
		else:
			reward = 0

		# episode_reward += reward
		agent.update(observation, action, reward, next_observation)

		observation = next_observation

		if done:
			print(i, " episode finished, ", j+1, " time step")
			break
