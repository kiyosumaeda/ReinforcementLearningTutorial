import matplotlib.pyplot as plt

"""
epsilon value
reward.txt -> 0.1
reward2.txt -> 0.01
reward3.txt -> 0
"""

def read_reward(l, filename):
	with open(filename, "r") as f:
		for row in f:
			l.append(float(row)/2000)

reward_list1 = []
reward_list2 = []
reward_list3 = []

read_reward(reward_list1, "reward.txt")
read_reward(reward_list2, "reward2.txt")
read_reward(reward_list3, "reward3.txt")

plt.figure(figsize=(12, 6))
plt.title("10-armed bandit")
plt.xlabel("step")
plt.ylabel("average reward")
plt.plot(reward_list1, color="blue", label="0.1")
plt.plot(reward_list2, color="red", label="0.01")
plt.plot(reward_list3, color="green", label="0")
plt.legend(loc=0)
plt.show()
