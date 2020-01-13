import gym

env_name = 'Breakout-v0'
episodes = 12000
first_steps = 30

env = gym.make(env_name)
agent = Agent(num_actions=env.action_space.n)

for i in range(episodes):
	is_finished = False
	observation = env.reset()
	for j in range(random.randint(1, first_steps)):
		latest_observation = observation
		observation, r, done, info = env.step(0)
	state = agent.get_initial_state(observation, latest_observation)
	while not is_finished:
		latest_observation = observation
		action = agent.get_action(state)
		observation, reward, is_finished, info = env.step(action)
		env.render()
		processed_observation = preprocess(observation, latest_observation)
		state = agent.run(state, action, reward, is_finished, processed_observation)