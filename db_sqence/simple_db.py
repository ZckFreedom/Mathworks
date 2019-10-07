import time

start_time = time.perf_counter()


def get_lexicographic_number(s_sequence):
	"""
	给定一个序列s，先得到序列的长度，并让序列循环两次
	之后取得序列的包含的所有最后一位是1的状态
	将状态按照字典序排列
	最后得到原序列在状态表中的位置和该循环序列包含的最后一位是1的状态个数
	"""
	size = len(s_sequence)
	s_sequence += s_sequence
	
	states = []
	for i in range(size):
		if s_sequence[i:i + size] not in states and s_sequence[i + size - 1] == 1:
			states.append(s_sequence[i:i + size])
	
	states.sort(reverse=True)
	return states.index(s_sequence[:size]), len(states)


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


class Shift_order_space:
	def __init__(self):
		self._shiftlist = []
		self._shiftnumber = 0
	
	def get_number(self):
		return self._shiftlist[-1][1]
	
	def len(self):
		return len(self._shiftlist)
	
	def apend(self, a_list):
		self._shiftlist.append((a_list, self._shiftnumber))
		self._shiftnumber += 1
	
	def if_not_in(self, a_list):
		if len(self._shiftlist) == 0:
			return True
		for i in range(0, len(self._shiftlist)):
			if self._shiftlist[i][0] == a_list:
				return False
		return True
	
	def select_sort(self):
		resort = self._shiftlist
		for i in range(0, len(resort) - 1):
			k = i
			for j in range(i, len(resort)):
				if resort[i][0] < resort[j][0]:
					k = j
			if i != k:
				resort[i], resort[k] = resort[k], resort[i]


def shift_order_first0(s_sequence):
	size = len(s_sequence)
	s_sequence += s_sequence
	
	real_states = Shift_order_space()
	for i in range(size, -1, -1):
		if real_states.if_not_in(s_sequence[i:i + size]) and s_sequence[i] == 0:
			real_states.apend((s_sequence[i:i + size]))
	
	real_states.select_sort()
	return real_states.get_number(), real_states.len()


def algorithm_C(s_sequence, t_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		k, m = shift_order_first0([0] + state[1:])
		if any([k == m - i and (m == i if i != t_number else True) for i in range(1, t_number + 1)]):
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


if __name__ == '__main__':
	algs = [('A', algorithm_A), ('B', algorithm_B), ('C', algorithm_C)]
	
	for n in range(5, 6):
		start = [0] * n
		for t in range(1, n):
			for kind, alg in algs:
				s = ''.join([str(x) for x in alg(start, t)])
				s += s
				idx = s.find('0' * len(start))
				print(n, t, kind, s[idx:idx + 2 ** (len(start))])

print(time.perf_counter() - start_time, "seconds")
