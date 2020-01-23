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

ACTION_INTERVAL = 4
INITIAL_REPLAY_SIZE = 20000

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
		y = tf.placeholder(tf.float32, [None])

		a_one_hot = tf.one_hot(a, self.num_actions, 1.0, 0.0)
		q_value = tf.reduce_sum(tf.mul(self.q_value, a_one_hot), reduction_indices=1)

		error = tf.abs(y - q_value)
		quadratic_part = tf.clip_by_value(error, 0.0, 1.0)
		linear_part = error - quadratic_part
		loss = tf.reduce_mean(0.5 * tf.square(quadratic_part) + linear_part)

		optimizer = tf.train.RMSPropOptimizer(LEARNING_RATE, momentum=MOMENTUM, epsilon=MIN_GRAD)
		grad_update = optimizer.minimize(loss, var_list=q_network_weights)

		return a, y, loss, grad_update

	def get_initial_state(self, observation, last_observation):
		processed_observation = np.maximum(observation, last_observation)
		processed_observation = np.uint8(resize(rgb2gray(processed_observation), (FRAME_WIDTH, FRAME_HEIGHT))*255)
		state = [processed_observation for i in range(STATE_LENGTH)]
		return np.stack(state, axis=0)

	def get_action(self, state):
		action = self.repeated_action

		if self.t % ACTION_INTERVAL == 0:
			if self.epsilon >= random.random() or self.t < INITIAL_REPLAY_SIZE:
				action = random.randomrange(self.num_actions)
			else:
				action = np.argmax(self.q_value.eval(feed_dict={self.x: [np.float32(state / 255.0)]}))
			self.repeated_action = action

		if self.epsilon > epsilon2 and self.t >= INITIAL_REPLAY_SIZE:
			self.epsilon -= self.epsilon_step

		return action
