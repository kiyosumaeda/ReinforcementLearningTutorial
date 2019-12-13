import gym
import numpy as np

GAMMA = 0.90
ETA = 0.01

class Brain:
	def __init__(self, num_states, num_actions):
		self.num_states = num_states
		self.num_actions = num_actions
		# self.q_table = np.random.uniform(low=0, high=1, size=(16, self.num_actions))
		self.q_table = np.zeros((16, self.num_actions))

	def bins(self, clip_min, clip_max, num):
		return np.linspace(clip_min, clip_max, num+1)[1:-1]

	def update_Qtable(self, observation, action, reward, observation_next):
		state = observation
		state_next = observation_next
		Max_Q_next = max(self.q_table[state_next][:])
		self.q_table[state, action] = self.q_table[state, action] + ETA*(reward+GAMMA*Max_Q_next - self.q_table[state, action])

	def decide_action(self, observation, episode):
		state = observation
		epsilon = 0.5*(1/(episode+1))
		# epsilon = 0.001

		if epsilon <= np.random.uniform(0, 1):
			action = np.argmax(self.q_table[state][:])
		else:
			action = np.random.choice(self.num_actions)
		return action
