import numpy as np

v = np.zeros(101)
policy = np.zeros(100)
p = 0.4
gamma = 0.9

threshold = 0.001

delta = 1
while delta >= threshold:
	delta = 0
	for s in range(1, 100):
		v_s = v[s]
		max_val = 0
		for a in range(0, min(s, 100-s)+1):
			head_capital = s + a
			tail_capital = s - a
			reward_head = 0
			reward_tail = 0
			if head_capital == 100:
				reward_head = 1
			head_val = p*(reward_head+gamma*v[head_capital])
			tail_val = (1-p)*(reward_tail+gamma*v[tail_capital])
			val = head_val + tail_val
			max_val = max(max_val, val)
		v[s] = max_val
		delta = max(delta, abs(v_s-v[s]))
	print(v)

for s in range(1, 100):
	dp = np.zeros(min(s, 100-s)+1)
	for a in range(0, min(s, 100-s)+1):
		head_capital = s+a
		tail_capital = s-a
		reward_head = 0
		reward_tail = 0
		if head_capital == 100:
			reward_head = 1
		head_val = p*(reward_head+gamma*v[head_capital])
		tail_val = (1-p)*(reward_tail+gamma*v[tail_capital])
		val = head_val+tail_val
		dp[a] = val
	policy[s] = np.argmax(dp)

print(policy)
