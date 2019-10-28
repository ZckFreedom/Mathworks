from check_out import check_out


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


def shift_order_first0(s_sequence):
	size = len(s_sequence)
	s_sequence += s_sequence
	
	real_states = Shift_order_space()
	for i in range(size, -1, -1):
		if real_states.if_not_in(s_sequence[i:i+size]) and s_sequence[i] == 0:
			real_states.apend((s_sequence[i:i + size]))
	
	real_states.select_sort()
	return real_states.get_number(), real_states.len()


def new_shift_order_first0(s_sequence):
	size = len(s_sequence)
	s_sequence += s_sequence
	
	real_states = Shift_order_space()
	for i in range(0, size):
		if real_states.if_not_in(s_sequence[i:i + size]) and s_sequence[i] == 0:
			real_states.apend((s_sequence[i:i + size]))
	
	real_states.select_sort()
	return real_states.get_number(), real_states.len()


def new_shift_order_first0_right(s_sequence):
	size = len(s_sequence)
	s_sequence += s_sequence
	
	real_states = Shift_order_space()
	for i in range(size, -1, -1):
		if real_states.if_not_in(s_sequence[i:i + size]) and s_sequence[i] == 0:
			real_states.apend((s_sequence[i:i + size]))
	
	real_states.select_sort()
	return real_states.get_number(), real_states.len()


def new_shift_order_last1(s_sequence):
	size = len(s_sequence)
	s_sequence += s_sequence
	
	real_states = Shift_order_space()
	for i in range(0, size):
		if real_states.if_not_in(s_sequence[i:i + size]) and s_sequence[i + size - 1] == 1:
			real_states.apend((s_sequence[i:i + size]))
	
	real_states.select_sort()
	return real_states.get_number(), real_states.len()


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


def lexi_order_alg_A(s_sequence, t_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		k, m = get_lexicographic_number_for0([0] + state[1:])
		if (m >= t_number and k == m - t_number) or (m < t_number and k == m - 1):
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
				if resort[k][0] < resort[j][0]:
					k = j
			if i != k:
				resort[i], resort[k] = resort[k], resort[i]


def shift_order_alg_A(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
			
		k, m = shift_order_first0([0] + state[1:])
		if (m % 2 == 1 and k == 0) or (m % 2 == 0 and k == 1):
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def shift_order_alg_B(s_sequence, t_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
			
		k, m = shift_order_first0([0] + state[1:])
		if (k == t_number - 1 and m >= t_number) or (k == 0 and m < t_number):
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def shift_order_alg_new_A(s_sequence, t_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		k, m = new_shift_order_first0([0] + state[1:])
		if k == t_number % m:
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def shift_order_alg_new_A_right(s_sequence, t_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		k, m = new_shift_order_first0_right([0] + state[1:])
		if k == t_number % m:
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def shift_order_alg_new_B(s_sequence, t_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		k, m = new_shift_order_last1(state[1:] + [1])
		if k == t_number % m:
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


if __name__ == '__main__':
	algs = [('C', lexi_order_alg_B),
	        ('C1', lexi_order_alg_A), ('D', shift_order_alg_A), ('E', shift_order_alg_B),
	        ('G1', shift_order_alg_new_A), ('G2', shift_order_alg_new_B)]
	
	class1 = ['G1', 'G2']
	class2 = ['C1', 'E']
	sequence_list = []

	for n in range(6, 7):
		start = [0] * n
		for kind, alg in algs:
			if kind in class1:
				cnt = 0
				for t in range(0, 60):
					s = ''.join([str(x) for x in alg(start, t)])
					s += s
					idx = s.find('0' * len(start))
					# if s[idx:idx + 2 ** (len(start))] not in sequence_list:
					# 	sequence_list.append(s[idx:idx + 2 ** (len(start))])
					# else:
					print(n, t, kind, s[idx:idx + 2 ** (len(start))])
				# 		cnt += 1
				# print(cnt)
					check_out(n, s)
			elif kind == 'E':
				for t in range(1, n):
					s = ''.join([str(x) for x in alg(start, t)])
					s += s
					idx = s.find('0' * len(start))
					# if s[idx:idx + 2 ** (len(start))] not in sequence_list:
					# 	sequence_list.append(s[idx:idx + 2 ** (len(start))])
					# else:
					print(n, t, kind, s[idx:idx + 2 ** (len(start))])
					check_out(n, s)
			elif kind == 'D':
				s = ''.join([str(x) for x in alg(start)])
				s += s
				idx = s.find('0' * len(start))
				# if s[idx:idx + 2 ** (len(start))] not in sequence_list:
				# 	sequence_list.append(s[idx:idx + 2 ** (len(start))])
				# else:
				print(n, kind, s[idx:idx + 2 ** (len(start))])
				check_out(n, s)
