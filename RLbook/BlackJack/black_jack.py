import random
import copy
import numpy as np

v = np.zeros((2, 10, 19))

returns = [[[0]*19]*10]*2
# print(returns)
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

episodes = 1
for i in range(episodes):
	player_cards_list = []
	reward_list = []
	player_cards = [cards[random.randrange(0, len(cards))], cards[random.randrange(0, len(cards))]]
	player_cards_list.append(player_cards)
	while (sum(player_cards_list[len(player_cards_list)-1]) < 20):
		current_player_cards = copy.copy(player_cards_list[len(player_cards_list)-1])
		current_player_cards.append(cards[random.randrange(0, len(cards))])
		if sum(current_player_cards) > 21:
			if 11 in current_player_cards:
				current_player_cards[current_player_cards.index(11)] = 1
			else:
				reward_list.append(-1)
		else:
			reward_list.append(0)
		player_cards_list.append(current_player_cards)
	print(player_cards_list)
	print(reward_list)
