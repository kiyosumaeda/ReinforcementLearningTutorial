import random
import copy
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

v = np.zeros((2, 10, 21))

# returns = [[[[0]*1]*21]*10]*2
returns = [[[[0 for i in range(1)] for j in range(21)] for k in range(10)] for l in range(2)]
# print(returns)
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

episodes = 10000
gamma = 1
for i in range(episodes):
	player_cards_list = []
	reward_list = []
	player_cards = [cards[random.randrange(0, len(cards))], cards[random.randrange(0, len(cards))]]
	player_cards_list.append(player_cards)
	current_player_cards = copy.copy(player_cards_list[len(player_cards_list)-1])
	while (sum(player_cards_list[len(player_cards_list)-1]) < 20):
		current_player_cards = copy.copy(player_cards_list[len(player_cards_list)-1])
		current_player_cards.append(cards[random.randrange(0, len(cards))])
		if sum(current_player_cards) > 21:
			if 11 in current_player_cards:
				current_player_cards[current_player_cards.index(11)] = 1
				reward_list.append(0)
			else:
				reward_list.append(-1)
		else:
			reward_list.append(0)
		player_cards_list.append(current_player_cards)

	dealer_cards = [cards[random.randrange(0, len(cards))], cards[random.randrange(0, len(cards))]]
	if (sum(current_player_cards) <= 21):
		while (sum(dealer_cards) < 17):
			dealer_cards.append(cards[random.randrange(0, len(cards))])

		player_cards_list.append(current_player_cards)
			
		if (sum(dealer_cards) > 21):
			reward_list.append(1)
		else:
			if (sum(dealer_cards) < sum(current_player_cards)):
				reward_list.append(1)
			elif (sum(dealer_cards) > sum(current_player_cards)):
				reward_list.append(-1)
			else:
				reward_list.append(0)
	# print(player_cards_list)
	# print(dealer_cards)
	# print(reward_list)

	g = 0
	T = len(reward_list)
	opened_card = dealer_cards[0]
	if (opened_card == 11):
		opened_card = 1
	for j in range(T):
		g = gamma*g + reward_list[T-j-1]
		st = player_cards_list[T-1-j]
		if (j != T-1):
			st1 = player_cards_list[T-2-j]
			if (sum(st) != sum(st1)):
				if (11 not in st):
					returns[1][opened_card-1][sum(st)-1].append(g)
					v[1][opened_card-1][sum(st)-1] = sum(returns[1][opened_card-1][sum(st)-1])/(len(returns[1][opened_card-1][sum(st)-1])-1)
				else:
					returns[0][opened_card-1][sum(st)-1].append(g)
					v[0][opened_card-1][sum(st)-1] = sum(returns[0][opened_card-1][sum(st)-1])/(len(returns[0][opened_card-1][sum(st)-1])-1)
		else:
			if (11 not in st):
				returns[1][opened_card-1][sum(st)-1].append(g)
				v[1][opened_card-1][sum(st)-1] = sum(returns[1][opened_card-1][sum(st)-1])/(len(returns[1][opened_card-1][sum(st)-1])-1)
			else:
				returns[0][opened_card-1][sum(st)-1].append(g)
				v[0][opened_card-1][sum(st)-1] = sum(returns[0][opened_card-1][sum(st)-1])/(len(returns[0][opened_card-1][sum(st)-1])-1)

print(returns)
print(v)

X = np.arange(11, 21, 1)
Y = np.arange(0, 10, 1)
mesh_X, mesh_Y = np.meshgrid(X, Y)
print(mesh_X)
print(mesh_Y)
Z_0 = v[0][:, 11:21]
Z_1 = v[1][:, 11:21]
print(Z_0)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("player sum")
ax.set_ylabel("dealer showing")

ax.plot_wireframe(X, Y, Z_0)
plt.show()
