def get_lexicographic_number(s_sequence):
	size = len(s_sequence)
	s_sequence += s_sequence
	
	states = []
	for i in range(size):
		if s_sequence[i:i + size] not in states and s_sequence[i + size - 1] == 1:
			states.append(s_sequence[i:i + size])
	
	states.sort(reverse=True)
	return states.index(s_sequence[:size]), len(states)


class Shift_order_space:
	def __init__(self):
		self._shiftlist = []
		self._shiftnumber = 0
	
	def get_number(self):
		return self._shiftlist[-1][1]
	
	def len(self):
		return len(self._shiftlist)
	
	def append(self, a_list):
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
			kk = i
			for j in range(i, len(resort)):
				if resort[i][0] < resort[j][0]:
					kk = j
			if i != kk:
				resort[i], resort[kk] = resort[kk], resort[i]


def shift_order_first0(s_sequence):
	size = len(s_sequence)
	s_sequence += s_sequence
	
	real_states = Shift_order_space()
	for i in range(size, -1, -1):
		if real_states.if_not_in(s_sequence[i:i + size]) and s_sequence[i] == 0:
			real_states.append((s_sequence[i:i + size]))
	
	real_states.select_sort()
	return real_states.get_number(), real_states.len()


def new_shift_order_first0(s_sequence):
	size = len(s_sequence)
	s_sequence += s_sequence
	
	real_states = Shift_order_space()
	for i in range(0, size):
		if real_states.if_not_in(s_sequence[i:i + size]) and s_sequence[i] == 0:
			real_states.append((s_sequence[i:i + size]))
	
	real_states.select_sort()
	return real_states.get_number(), real_states.len()


def new_shift_order_last1(s_sequence):
	size = len(s_sequence)
	s_sequence += s_sequence
	
	real_states = Shift_order_space()
	for i in range(0, size):
		if real_states.if_not_in(s_sequence[i:i + size]) and s_sequence[i + size - 1] == 1:
			real_states.append((s_sequence[i:i + size]))
	
	real_states.select_sort()
	return real_states.get_number(), real_states.len()


def algorithm_B(s_sequence, t_number):      # B1
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		kk, m = get_lexicographic_number(state[1:] + [1])
		if (m >= t_number and kk == m - t_number) or (m < t_number and kk == m - 1):
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def algorithm_A(s_sequence, k_number, t_number):  # B2
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		kk, m = get_lexicographic_number(state[1:] + [1])
		if (kk == m - k_number and m >= k_number) or (kk == m - t_number and t_number <= m < k_number) or (kk == m - 1 and m < t_number):
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def lexi_order_alg_B(s_sequence):       # B3
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		kk, m = get_lexicographic_number(state[1:] + [1])
		if (m % 2 == 1 and kk == m - 1) or (m % 2 == 0 and kk == m - 2):
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def shift_order_alg_A(s_sequence, t_number):      # D1
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		kk, m = shift_order_first0([0] + state[1:])
		if (kk == t_number - 1 and m >= t_number) or (kk == 0 and m < t_number):
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def shift_order_alg_B(s_sequence, k_number, t_number):  # D2
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		kk, m = shift_order_first0([0] + state[1:])
		if (kk == k_number - 1 and m >= k_number) or (kk == t_number - 1 and t_number <= m < k_number) or (kk == 0 and m < t_number):
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def shift_order_alg_C(s_sequence):      # D3
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		kk, m = shift_order_first0([0] + state[1:])
		if (m % 2 == 1 and kk == 0) or (m % 2 == 0 and kk == 1):
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def shift_order_alg_new_A(s_sequence, t_number):    # H1
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		kk, m = new_shift_order_first0([0] + state[1:])
		if kk == t_number % m:
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def shift_order_alg_new_B(s_sequence, t_number):    # H2
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		kk, m = new_shift_order_last1(state[1:] + [1])
		if kk == t_number % m:
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


if __name__ == '__main__':
	algs = [('B1', algorithm_B), ('B2', algorithm_A), ('B3', lexi_order_alg_B),
	        ('D1', shift_order_alg_A), ('D2', shift_order_alg_B), ('D3', shift_order_alg_C),
	        ('H1', shift_order_alg_new_A), ('H2', shift_order_alg_new_B)]
	class1 = ['B3', 'D3']
	class2 = ['B2', 'D2']
	class3 = ['H1', 'H2']
	
	for n in range(4, 5):
		start = [0] * n
		for kind, alg in algs:
			if kind in class1:
				s = ''.join([str(x) for x in alg(start)])
				s += s
				idx = s.find('0' * len(start))
				print(n, kind, s[idx:idx + 2 ** (len(start))])
			elif kind in class2:
				for t in range(2, n):
					for k in range(1, t):
						s = ''.join([str(x) for x in alg(start, t, k)])
						s += s
						idx = s.find('0' * len(start))
						print(n, t, k, kind, s[idx:idx + 2 ** (len(start))])
			elif kind in class3:
				for t in range(0, 60):
					s = ''.join([str(x) for x in alg(start, t)])
					s += s
					idx = s.find('0' * len(start))
					print(n, t, kind, s[idx:idx + 2 ** (len(start))])
			else:
				for t in range(1, n):
					s = ''.join([str(x) for x in alg(start, t)])
					s += s
					idx = s.find('0' * len(start))
					print(n, t, kind, s[idx:idx + 2 ** (len(start))])
