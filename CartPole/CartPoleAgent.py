import gym
import numpy as np


GAMMA = 0.0
alpha = 0.1
digitized_num = 6

class Agent:
	def __init__(self, states_num, actions_num):
		self.actions_num = actions_num
		self.q = np.zeros((digitized_num**states_num, actions_num))

	def digitize_state(self, observation):
		cart_pos, cart_v, pole_angle, pole_v = observation

		digitized = [
			np.digitize(cart_pos, bins=np.linspace(-2.4, 2.4, digitized_num+1)[1:-1]),
			np.digitize(cart_v, bins=np.linspace(-3.0, 3.0, digitized_num+1)[1:-1]),
			np.digitize(pole_angle, bins=np.linspace(-0.5, 0.5, digitized_num+1)[1:-1]),
			np.digitize(pole_v, bins=np.linspace(-2.0, 2.0, digitized_num+1)[1:-1])
		]
		return sum([x*(digitized_num**i) for i, x in enumerate(digitized)])

	def update(self, observation, action, reward, next_observation):
		state = self.digitize_state(observation)
		next_state = self.digitize_state(next_observation)
		next_q = max(self.q[next_state][:])
		self.q[state, action] += alpha*(reward+GAMMA*next_q - self.q[state, action])

	def take_action(self, observation, episode):
		state = self.digitize_state(observation)
		epsilon = 0.5*(1/(episode+1))
		if epsilon <= np.random.uniform(0, 1):
			action = np.argmax(self.q[state][:])
		else:
			action = np.random.choice(self.actions_num)
		return action
