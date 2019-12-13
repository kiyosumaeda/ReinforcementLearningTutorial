import gym

from FrozenLakeBrain import Brain

class Agent:
	def __init__(self, num_states, num_actions):
		self.num_states = num_states
		self.num_actions = num_actions
		self.brain = Brain(num_states, num_actions)

	def update_q_functions(self, observation, action, reward, observation_next):
		self.brain.update_Qtable(observation, action, reward, observation_next)

	def get_action(self, observation, step):
		action = self.brain.decide_action(observation, step)
		return action
