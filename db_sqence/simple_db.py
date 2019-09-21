import time

start_time = time.perf_counter()


def get_lexicographic_number(s_sqeuence):
	"""
	给定一个序列s，先得到序列的长度，并让序列循环两次
	之后取得序列的包含的所有最后一位是1的状态
	将状态按照字典序排列
	最后得到原序列在状态表中的位置和该循环序列包含的最后一位是1的状态个数
	"""
	size = len(s_sqeuence)
	s_sqeuence += s_sqeuence
	
	states = []
	for i in range(size):
		if s_sqeuence[i:i + size] not in states and s_sqeuence[i + size - 1] == 1:
			states.append(s_sqeuence[i:i + size])
	
	states.sort(reverse=True)
	return states.index(s_sqeuence[:size]), len(states)


def algorithm_A(s_sequence, t_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		k, m = get_lexicographic_number(state[1:] + [1])
		if any([k == m - i and (m == i if i != t_number else True) for i in range(1, t_number + 1)]):
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def algorithm_B(s_sequence, t_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		k, m = get_lexicographic_number(state[1:] + [1])
		if (m >= t_number and k == m - t_number) or (m < t_number and k == m - 1):
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


if __name__ == '__main__':
	algs = [('A', algorithm_A), ('B', algorithm_B)]
	
	for n in range(5, 6):
		start = [0] * n
		for t in range(1, n):
			for kind, alg in algs:
				s = ''.join([str(x) for x in alg(start, t)])
				s += s
				idx = s.find('0' * len(start))
				print(n, t, kind, s[idx:idx + 2 ** (len(start))])

print(time.perf_counter() - start_time, "seconds")
