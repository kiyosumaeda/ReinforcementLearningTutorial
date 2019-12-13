import gym

from FrozenLakeAgent import Agent

ENV = 'FrozenLake-v0'
MAX_STEPS = 100
NUM_EPISODES = 10000

class Environment:
	def __init__(self):
		self.env = gym.make(ENV)
		# self.num_states = self.env.observation_space.shape[0]
		self.num_states = 1
		self.num_actions = self.env.action_space.n
		self.agent = Agent(self.num_states, self.num_actions)
		self.all_episode_list = []

	def run(self):
		complete_episodes = 0
		episode_final = False

		for episode in range(NUM_EPISODES):
			observation = self.env.reset()
			episode_reward = 0

			for step in range(MAX_STEPS):
				# self.env.render()
				action = self.agent.get_action(observation, episode)
				observation_next, reward_notuse, done, info_notuse = self.env.step(action)

				if done:
					if observation_next == 15:
						complete_episodes += 1
						reward = 1
						self.all_episode_list.append(1)
						print("success!!!!")
					else:
						reward = -1
						self.all_episode_list.append(0)
						print("failed...")
				else:
					reward = 0

				episode_reward += reward

				self.agent.update_q_functions(
					observation, action, reward, observation_next
				)

				observation = observation_next

				if done:
					print('{0} Episode: Finished after {1} time steps'.format(episode, step+1))
					break

				if step == MAX_STEPS-1:
					self.all_episode_list.append(0)

			# if self.complete_episodes >= 10:
			# 	print('10回連続成功')
			# 	frames = []
			# 	episode_final = True
		print('success episodes: ', complete_episodes)

	def show_episode_list(self):
		with open("episode3.txt", "wt") as f:
			for episode in self.all_episode_list:
				f.write(str(episode)+'\n')
