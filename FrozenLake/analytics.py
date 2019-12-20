import matplotlib.pyplot as plt

"""
episode1: gamma->0.99, eta->0.1
episode2: gamma->0.95, eta->0.1
episode3: gamma->0.90, eta->0.1
3-2: epsilon->0.01
3-3: epsilon->0.1
"""

episode_list = []
sum = 0
count = 0
with open("episode1.txt", "r") as f:
	for row in f:
		if count < 100:
			sum += int(row)
			count += 1
		else:
			episode_list.append(sum)
			sum = 0
			count = 0
		# sum += int(row)
		# episode_list.append(sum)

def read_reward(l, filename):
	with open(filename, "r") as f:
		for row in f:
			if len(l) == 0:
				l.append(int(row))
			else:
				current = l[len(l)-1]
				l.append((current*len(l)+int(row))/(len(l)+1))


reward_list1 = []
reward_list2 = []
reward_list3 = []

read_reward(reward_list1, "episode1.txt")
read_reward(reward_list2, "episode2.txt")
read_reward(reward_list3, "episode3.txt")

print(reward_list1)

plt.figure(figsize=(12, 6))
plt.title("frozen lake")
plt.xlabel("episode")
plt.ylabel("success rate")
plt.plot(reward_list1, color="blue", label="0.99")
plt.plot(reward_list2, color="red", label="0.95")
plt.plot(reward_list3, color="green", label="0.90")
plt.legend(loc=0)
plt.show()

# print(episode_list)
# plt.plot(episode_list)
# plt.show()
