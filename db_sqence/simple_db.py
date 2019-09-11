import time

start_time = time.perf_counter()


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
		if s[i:i + size] not in states and s[i + size - 1] == 1:
			states.append(s[i:i + size])
	
	states.sort(reverse=True)
	return states.index(s[:size]), len(states)


def algorithm_A(s, t):
	state = None
	retval = []
	
	while state != s:
		if state is None:
			state = s[:]
		
		k, m = get_lexicographic_number(state[1:] + [1])
		if any([k == m - i and (m == i if i != t else True) for i in range(1, t + 1)]):
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def algorithm_B(s, t):
	state = None
	retval = []
	
	while state != s:
		if state is None:
			state = s[:]
		
		k, m = get_lexicographic_number(state[1:] + [1])
		if (m >= t and k == m - t) or (m < t and k == m - 1):
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


if __name__ == '__main__':
	algs = [('A', algorithm_A), ('B', algorithm_B)]
	
	for n in range(5, 11):
		start = [0] * n
		for t in range(1, n):
			for kind, alg in algs:
				s = ''.join([str(x) for x in alg(start, t)])
				s += s
				idx = s.find('0' * len(start))
				print(n, t, kind, s[idx:idx + 2 ** (len(start))])

print(time.perf_counter() - start_time, "seconds")
