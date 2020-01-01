import matplotlib.pyplot as plt

"""
step1.txt alpha=0.1, gamma=0.90
step2.txt alpha=0.1, gamma=0.99
step3.txt alpha=0.1, gamma=0.0
"""

def read_reward(l, filename):
	with open(filename, "r") as f:
		for row in f:
			if (len(l)>0):
				l.append((int(row)+l[len(l)-1]*len(l))/(len(l)+1))
			else:
				l.append(int(row))

reward_list1 = []
reward_list2 = []
reward_list3 = []

read_reward(reward_list1, "step1.txt")
read_reward(reward_list2, "step2.txt")
read_reward(reward_list3, "step3.txt")

plt.figure(figsize=(12, 6))
plt.title("CartPole")
plt.xlabel("episode")
plt.ylabel("average step")
plt.plot(reward_list1, color="red", label="0.90")
plt.plot(reward_list2, color="blue", label="0.99")
plt.plot(reward_list3, color="green", label="0.0")
plt.legend(loc=0)
plt.show()
