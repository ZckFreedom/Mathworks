from check_out import check_out


def find_nk(s_sequence):
	size = len(s_sequence)
	state = s_sequence[:size-1]
	state += state
	states = []
	
	for i in range(0, size - 1):
		if state[i: i + size] not in states:
			states.append(state[i: i + size])
	
	states.sort()
	return states[0]


def find_conk(s_sequence):
	size = len(s_sequence)
	state = s_sequence[:size - 1]
	state += [1 - x for x in state]
	state += s_sequence
	states = []
	
	for i in range(0, 2 * size - 1):
		if state[i: i + size] not in states:
			states.append(state[i: i + size])
	
	states.sort()
	return states[0]


def find_rnk(s_sequence):
	size = len(s_sequence)
	state = s_sequence[:size - 1]
	state += state
	states = []
	
	for i in range(0, size - 1):
		if state[i: i + size] not in states:
			states.append(state[i: i + size])
	
	states.sort()
	return states[-1]


def find_rconk(s_sequence):
	size = len(s_sequence)
	state = s_sequence[:size - 1]
	state += [1 - x for x in state]
	state += s_sequence
	states = []
	
	for i in range(0, 2 * size - 1):
		if state[i: i + size] not in states:
			states.append(state[i: i + size])
	
	states.sort()
	return states[-1]


def alg_nkorenk_A(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		answer = None
		if state[1:] == [1] * (len(state) - 1):
			answer = True
		elif state[-1] == 1:
			next_state = state[1:] + [0]
			answer = (next_state == find_nk(next_state))
		elif state[-1] == 0:
			next_state = state[1:] + [1]
			answer = (next_state == find_conk(next_state))
			
		if answer is True:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_nkorrnk_B(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		next_state = state[1:] + [0]
		if next_state[0] == 1 and next_state == find_rconk(next_state):
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		elif next_state[0] == 0 and next_state == find_nk(next_state):
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_nkorrnk_C(s_sequence):
	"""
	与算法B生成的序列是互补的序列
	"""
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		next_state = state[1:] + [1]
		if next_state[0] == 1 and next_state == find_rnk(next_state):
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		elif next_state[0] == 0 and next_state == find_conk(next_state):
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
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
			k = i
			for j in range(i, len(resort)):
				if resort[k][0] < resort[j][0]:
					k = j
			if i != k:
				resort[i], resort[k] = resort[k], resort[i]


def shift_order(s_sequence):
	size = len(s_sequence) - 1
	count_size = size
	state = s_sequence[:size]
	if s_sequence[-1] == 1:
		state += [1 - x for x in state]
		state += state
		count_size = size * 2
	elif s_sequence[-1] == 0:
		state += state
	
	states = Shift_order_space()
	for i in range(0, count_size):
		if states.if_not_in(state[i:i + size + 1]) and state[i] == 0:
			states.append(state[i:i + size + 1])
	
	states.select_sort()
	return states.get_number(), states.len()


def alg_shift_order(s_sequence, k_number):
	"""
	对于k为2的时候能够生成dB序列
	"""
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		change_state = [0] + state[1:]
		local, shift_len = shift_order(change_state)
		if shift_len >= k_number and local == k_number - 1:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		elif shift_len < k_number and local == 0:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


# algs = [('A', alg_nkorenk_A), ('B', alg_nkorrnk_B)]
# for kind, alg in algs:
# 	start = [0]*10
# 	s = ''.join([str(x) for x in alg(start)])
# 	s += s
# 	idx = s.find('0' * len(start))
# 	print(kind, s[idx:idx + 2 ** (len(start))])
# 	print(len(s))
start = [0] * 5
s = ''.join([str(x) for x in alg_shift_order(start, 4)])
s += s
idx = s.find('0' * len(start))
# print(s[idx:idx + 2 ** (len(start))])
print(len(s))
print(check_out(5, s))
