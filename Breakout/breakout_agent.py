import tensorflow as tf
from keras.models import Sequential
from keras.layers import Convolution2D, Flatten, Dense
from collections import deque

epsilon1 = 1.0
epsilon2 = 0.1
exploration_steps = 1000000

STATE_LENGTH = 4
FRAME_WIDTH = 84
FRAME_HEIGHT = 84

LEARNING_RATE = 0.00025
MOMENTUM = 0.95
MIN_GRAD = 0.01

class Agent():
	def __init__(self, num_actions):
		self.num_actions = num_actions
		self.epsilon = epsilon1
		self.epsilon_step = (epsilon1 - epsilon2)/exploration_steps
		self.time_steps = 0
		self.repeated_action = 0

		self.replay_memory = deque()

		self.s, self.q_value, self.q_network = self.build_network()
		q_network_weights = q_network.trainable_weights

		self.st, self.target_q_values, target_network = self.build_network()
		target_network_weights = target_network.trainable_weights

		self.update_target_network = [target_network_weights[i].assign(q_network_weights[i]) for i in range(len(target_network_weights))]

		self.a, self.y, self.loss, self.grad_update = self.build_training_op(q_network_weights)

		self.sess = tf.InteractiveSession()

		self.sess.run(tf.initialize_all_variables())

		self.sess.run(self.update_target_network)

	def build_network(self):
		model = Sequential()
		model.add(Convolution2D(32, 8, 8, subsample=(4, 4), activation='relu', input_shape=(STATE_LENGTH, FRAME_WIDTH, FRAME_HEIGHT)))
		model.add(Convolution2D(64, 4, 4, subsample=(2, 2), activation='relu'))
		model.add(Convolution2D(64, 3, 3, subsample=(1, 1), activation='relu'))
		model.add(Flatten())
		model.add(Dense(512, activation='relu'))
		model.add(Dense(self.num_actions))

		s = tf.placeholder(tf.float32, [None, STATE_LENGTH, FRAME_WIDTH, FRAME_HEIGHT])
		q_values = model(s)
		
		return s, q_values, model

	def build_training_op(self, q_network_weights):
		a = tf.placeholder(tf.int64, [None])
