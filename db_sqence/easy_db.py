def get_lexicographic_number(s):
	"""
	给定一个序列s，先得到序列的长度，并让序列循环两次
	之后取得序列的包含的所有最后一位是1的状态
	将状态按照字典序排列
	最后得到原序列在状态表中的位置和该循环序列包含的最后一位是1的状态个数
	"""
	size = len(s)
	s += s
	
	states = []
	for i in range(size):
		if s[i:i + size] not in states:
			states.append(s[i:i + size])
	
	states.sort(reverse=True)
	return states.index(s[:size]), len(states)

def weight_order_alg_A(s):
	state = None
	retval = []
	
	while state != s:
		if state is None:
			state = s[:]
		
		k, m = get_lexicographic_number(state[1:] + [1])
		if k == m-1:
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
		
	return retval


def weigth_order_alg_B(s):
	state = None
	retval = []
	
	while state != s:
		if state is None:
			state = s[:]
		
		k, m = get_lexicographic_number([0] + state[1:])
		if k == m - 1:
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
		
	return retval


if __name__ == '__main__':
	algs = [('A', weight_order_alg_A), ('B', weigth_order_alg_B)]
	
	for n in range(3, 5):
		start = [0] * n
		for t in range(1, n):
			for kind, alg in algs:
				s = ''.join([str(x) for x in alg(start)])
				s += s
				idx = s.find('0' * len(start))
				print(n, t, kind, s[idx:idx + 2 ** (len(start))])

