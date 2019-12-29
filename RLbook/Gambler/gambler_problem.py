import numpy as np
import matplotlib.pyplot as plt

v = np.zeros(101)
policy = np.zeros(100)
p = 0.4
# gamma = 0.9
gamma = 1.0

threshold = 0.000001
sweep = []

delta = 1
iteration = 0
# while delta >= threshold:
while iteration <= 32:
	delta = 0
	for s in range(1, 100):
		v_s = v[s]
		max_val = 0
		for a in range(0, min(s, 100-s)+1):
			head_capital = s + a
			tail_capital = s - a
			reward_head = 0.0
			reward_tail = 0.0
			if head_capital >= 100:
				reward_head = 1.0
			head_val = p*(reward_head+gamma*v[head_capital])
			tail_val = (1-p)*(reward_tail+gamma*v[tail_capital])
			val = head_val + tail_val
			max_val = max(max_val, val)
		v[s] = max_val
		delta = max(delta, abs(v_s-v[s]))
	print(v)
	sweep.append(v.copy())
	iteration += 1

print(len(sweep))
x = np.linspace(1, 99, 99)
# fig = plt.figure(figsize=(12, 6))
# ax = fig.add_subplot(111)
# ax.plot(x, sweep[0][1:100])
# ax.plot(x, sweep[1][1:100])

for s in range(1, 100):
	dp = np.zeros(min(s, 100-s)+1)
	for a in range(1, min(s, 100-s)+1):
		head_capital = s+a
		tail_capital = s-a
		reward_head = 0.0
		reward_tail = 0.0
		if head_capital == 100:
			reward_head = 1.0
		head_val = p*(reward_head+gamma*v[head_capital])
		tail_val = (1-p)*(reward_tail+gamma*v[tail_capital])
		val = head_val+tail_val
		dp[a] = val
	policy[s] = np.argmax(dp)

print(policy)

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)
ax.plot(x, policy[1:100])
plt.legend()
plt.show()
