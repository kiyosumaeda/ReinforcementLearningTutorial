import random
import copy
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

policy = np.zeros((2, 10, 21))
policy[:, :, 19:] = 1
q = np.zeros((2, 2, 10, 21))
returns = [[[[[0 for i in range(1)] for j in range(21)] for k in range(10)] for l in range(2)] for m in range(2)]
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
# print(policy)

episodes = 1
gamma = 1
for i in range(episodes):
	print("episode: ", i)
	usable_ace = random.randrange(0, 2)
	current_sum = 0
	dealer_showing_card = cards[random.randrange(0, len(cards))]
	if dealer_showing_card==11:
		dealer_showing_card = 1
	if usable_ace==0:
		current_sum = random.randrange(12, 22)
	else:
		current_sum = random.randrange(4, 21)
	print(usable_ace, current_sum, dealer_showing_card)

	player_sum_list = [current_sum]
	action_list = []
	aces = [usable_ace]
	reward_list = []
	while(policy[usable_ace][dealer_showing_card-1][current_sum-1]==0):
		action_list.append(0)
		new_card = cards[random.randrange(0, len(cards))]
		print("new card: ", new_card)
		if (current_sum+new_card>21):
			if (new_card==11):
				new_current_sum = current_sum+1
				current_sum = new_current_sum
				player_sum_list.append(new_current_sum)
				aces.append(usable_ace)
				reward_list.append(0)
			else:
				if usable_ace==0:
					new_current_sum = current_sum - 10 + new_card
					current_sum = new_current_sum
					player_sum_list.append(new_current_sum)
					usable_ace = 1
					aces.append(1)
					reward_list.append(0)
				else:
					current_sum += new_card
					player_sum_list.append(current_sum)
					aces.append(usable_ace)
					reward_list.append(-1)
					break
		else:
			new_current_sum = current_sum+new_card
			current_sum = new_current_sum
			player_sum_list.append(new_current_sum)
			aces.append(usable_ace)
			reward_list.append(0)

	if current_sum<= 21:
		action_list.append(1)

	dealer_cards = []
	dealer_cards.append(dealer_showing_card)
	dealer_cards.append(cards[random.randrange(0, len(cards))])
	if (current_sum <= 21):
		while(sum(dealer_cards) < 17):
			dealer_cards.append(cards[random.randrange(0, len(cards))])

		# player_sum_list.append(current_sum)

		if (sum(dealer_cards) > 21):
			reward_list.append(1)
		else:
			if (sum(dealer_cards) < current_sum):
				reward_list.append(1)
			elif (sum(dealer_cards) > current_sum):
				reward_list.append(-1)
			else:
				reward_list.append(0)

	print(player_sum_list)
	print(action_list)
	print(aces)
	print(sum(dealer_cards))
	print(reward_list)

	g = 0
	T = len(reward_list)
	for j in range(T):
		g = gamma*g + reward_list[T-j-1]
		st = player_sum_list[T-1-j]
		have_ace = aces[T-1-j]
		action = action_list[T-1-j]
		print(g, st, have_ace, action)
		if (j != T-1):
			st1 = player_sum_list[T-2-j]
			if (st != st1):
				returns[action][have_ace][dealer_showing_card-1][st-1].append(g)
				q[action][have_ace][dealer_showing_card-1][st-1] = sum(returns[action][have_ace][dealer_showing_card-1][st-1])/(len(returns[action][have_ace][dealer_showing_card-1][st-1])-1)
		else:
			returns[action][have_ace][dealer_showing_card-1][st-1].append(g)
			q[action][have_ace][dealer_showing_card-1][st-1] = sum(returns[action][have_ace][dealer_showing_card-1][st-1])/(len(returns[action][have_ace][dealer_showing_card-1][st-1])-1)
		q0 = q[0][have_ace][dealer_showing_card-1][st-1]
		q1 = q[1][have_ace][dealer_showing_card-1][st-1]
		print(q0, q1)
		if (q0 > q1):
			policy[have_ace][dealer_showing_card-1][st-1] = 0
		else:
			policy[have_ace][dealer_showing_card-1][st-1] = 1
	print(policy)
