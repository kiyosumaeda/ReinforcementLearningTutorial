import matplotlib.pyplot as plt

def read_reward(l, filename):
	with open(filename, "r") as f:
		for row in f:
			l.append(float(row))

q_reward = []
sarsa_reward = []
read_reward(q_reward, "cliff_q.txt")
read_reward(sarsa_reward, "cliff_sarsa.txt")

plt.figure(figsize=(12, 6))
plt.title("q learning and sarsa")
plt.xlabel("Episodes")
plt.plot(q_reward, color="red", label="Q-learning")
plt.plot(sarsa_reward, color="blue", label="Sarsa")
plt.ylim(-100, -20)
plt.show()

