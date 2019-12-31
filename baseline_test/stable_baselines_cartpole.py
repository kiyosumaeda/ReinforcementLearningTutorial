import gym
from stable_baselines.bench import Monitor
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2

env = gym.make('CartPole-v1')
env = DummyVecEnv([lambda: env])

model = PPO2(total_timesteps=10000)

state = env.reset()
for i in range(200):
	env.render()
	action, _ = model.predict(state)
	state, reward, done, info = env.step(action)
