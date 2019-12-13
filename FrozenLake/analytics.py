import matplotlib.pyplot as plt

episode_list = []
sum = 0
count = 0
with open("episode3.txt", "r") as f:
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

print(episode_list)
# plt.plot(episode_list)
# plt.show()
