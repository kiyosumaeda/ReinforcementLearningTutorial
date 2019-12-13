import gym
import numpy as np

NUM_DIZITIZED = 6
GAMMA = 0.99
ETA = 0.5

class Brain:
	def __init__(self, num_states, num_actions):
		self.num_states = num_states
		self.num_actions = num_actions
		self.q_table = np.random.uniform(low=0, high=1, size=(NUM_DIZITIZED**self.num_states, self.num_actions))

	def bins(self, clip_min, clip_max, num):
		return np.linspace(clip_min, clip_max, num+1)[1:-1]

	def digitize_state(self, observation):
		cart_pos, cart_v, pole_angle, pole_v = observation
		digitized = [
			np.digitize(cart_pos, bins=self.bins(-2.4, 2.4, NUM_DIZITIZED)),
			np.digitize(cart_v, bins=self.bins(-3.0, 3.0, NUM_DIZITIZED)),
			np.digitize(pole_angle, bins=self.bins(-0.5, 0.5, NUM_DIZITIZED)),
			np.digitize(pole_v, bins=self.bins(-2.0, 2.0, NUM_DIZITIZED))
		]
		return sum([x*(NUM_DIZITIZED**i) for i, x in enumerate(digitized)])

	def update_Qtable(self, observation, action, reward, observation_next):
		state = self.digitize_state(observation)
		state_next = self.digitize_state(observation_next)
		Max_Q_next = max(self.q_table[state_next][:])
		self.q_table[state, action] = self.q_table[state, action] + ETA*(reward+GAMMA*Max_Q_next - self.q_table[state, action])

	def decide_action(self, observation, episode):
		state = self.digitize_state(observation)
		epsilon = 0.5*(1/(episode+1))

		if epsilon <= np.random.uniform(0, 1):
			action = np.argmax(self.q_table[state][:])
		else:
			action = np.random.choice(self.num_actions)
		return action
