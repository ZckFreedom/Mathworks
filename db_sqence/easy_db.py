def get_lexicographic_number_for0(s_sequence):
	size = len(s_sequence)
	s_sequence += s_sequence
	
	states = []
	for i in range(size):
		if s_sequence[i:i + size] not in states and s_sequence[i] == 0:
			states.append(s_sequence[i:i + size])
	
	states.sort(reverse=True)
	return states.index(s_sequence[:size]), len(states)


def lexicographic_number(s_sequence):
	"""
	得到所有移位状态，之后按照字典序排序
	将状态按照字典序排列
	最后得到原序列在状态表中的位置和该循环序列长度
	主要求是否是necklace
	"""
	size = len(s_sequence)
	s_sequence += s_sequence
	
	states = []
	for i in range(size):
		if s_sequence[i:i + size] not in states:
			states.append(s_sequence[i:i + size])
	
	states.sort(reverse=True)
	return states.index(s_sequence[:size]), len(states)


def shift_order(s_sequence):
	size = len(s_sequence)
	s_sequence += s_sequence
	cnt = 0
	
	states = []
	real_states = []
	for i in range(size, -1, -1):
		if s_sequence[i:i+size] not in states and s_sequence[i] == 0:
			sequence_number = Shift_order_space(s_sequence[i:i + size], cnt)
			states.append(s_sequence[i:i + size])
			real_states.append(sequence_number)
			cnt += 1
	
	real_states.sort(reverse=True)
	return real_states[-1].get_number(), len(real_states)


def weight_order_alg_A(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		k, m = lexicographic_number(state[1:] + [1])
		if k == m-1:
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
		
	return retval


def weigth_order_alg_B(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		k, m = lexicographic_number([0] + state[1:])
		if k == m - 1:
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
		
	return retval


def lexi_order_alg_A(s_sequence, t):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		k, m = get_lexicographic_number_for0([0] + state[1:])
		if (m >= t and k == m - t) or (m < t and k == m - 1):
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
		
	return retval


def lexi_order_alg_B(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		k, m = get_lexicographic_number_for0([0] + state[1:])
		if (m % 2 == 1 and k == m-1) or (m % 2 == 0 and k == m-2):
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
	
		retval.append(state[-1])
		
	return retval


class Shift_order_space:
	def __init__(self, a_list, shift_number):
		self._shiftlist = a_list
		self._shiftnumber = shift_number
	
	def get_list(self):
		return self._shiftlist
	
	def get_number(self):
		return self._shiftnumber
	
	def __lt__(self, other):
		return self._shiftlist < other.get_list()
	
	def __eq__(self, other):
		return self._shiftlist == other.get_list()
	
	def __gt__(self, other):
		return self._shiftlist > other.get_list()


def shift_order_alg_A(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		k, m = shift_order([0] + state[1:])
		if (m % 2 == 1 and k == 0) or (m % 2 == 0 and k == 1):
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


if __name__ == '__main__':
	algs = [('A', weight_order_alg_A), ('B', weigth_order_alg_B), ('C', lexi_order_alg_B), ('D', shift_order_alg_A)]

	for n in range(3, 8):
		start = [0] * n
		for kind, alg in algs:
			s = ''.join([str(x) for x in alg(start)])
			s += s
			idx = s.find('0' * len(start))
			print(n, kind, s[idx:idx + 2 ** (len(start))])

