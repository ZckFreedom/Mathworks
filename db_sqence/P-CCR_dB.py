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


def lexi_order(s_sequence):
	size = len(s_sequence)
	reference_state = s_sequence[:size-1]
	reference_state += reference_state
	states = []
	
	for i in range(0, size - 1):
		if reference_state[i:i + size] not in states and reference_state[i] == 0:
			states.append(reference_state[i:i + size])
	
	states.sort()
	return states.index(s_sequence), len(states)
	

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
	
	def find_sequence(self, a_list):
		for i in range(0, len(self._shiftlist)):
			if a_list == self._shiftlist[i][0]:
				return self._shiftlist[i][1]
	
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
	state = s_sequence[:size]
	state += state
	
	states = Shift_order_space()
	for i in range(0, size):
		if states.if_not_in(state[i:i + size + 1]) and state[i] == 0:
			states.append(state[i:i + size + 1])
	
	states.select_sort()
	return states.get_number(), states.len()


def shift_order_for_1(s_sequence):
	size = len(s_sequence) - 1
	necklace = find_nk(s_sequence)
	necklace = necklace[:size]
	necklace += necklace
	
	states = Shift_order_space()
	for i in range(size-1, -1, -1):
		if states.if_not_in(necklace[i:i + size + 1]) and necklace[i] == 1:
			states.append(necklace[i:i + size + 1])
	
	return states.find_sequence(s_sequence), states.len()


def alg_nkorrnk_D1(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		local, lexi_len = None, None
		next_state = state[1:] + [1]
		if next_state[0] == 1:
			local, lexi_len = lexi_order(next_state)
		
		if next_state[0] == 0 and next_state == find_conk(next_state):
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		elif next_state[0] == 1 and ((lexi_len % 2 == 1 and local == 0) or (lexi_len % 2 == 0 and local == 1)):
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_nkorrnk_D2(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		answer = None
		if state[-1] == 1:
			gamma_state = []
			for i in range(1, len(state) - 1):
				gamma_state.append(1 - state[i])
			gamma_state += [0, state[1]]
			answer = (gamma_state == find_conk(gamma_state))
		elif state[-1] == 0:
			local, lexi_len = lexi_order([0] + state[1:])
			lens = lexi_len % 4
			if lens == 0:
				lens = 4
			answer = local == lens - 1
		
		if answer:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_nkorrnk_D3(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		local, lexi_len, lens = None, None, None
		next_state = state[1:] + [1]
		if next_state[0] == 1:
			local, lexi_len = lexi_order(next_state)
			lens = lexi_len % 1
		if lens == 0:
			lens = 1
		
		if next_state[0] == 0 and next_state == find_conk(next_state):
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		elif next_state[0] == 1 and local == lens - 1:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_shift_orderA(s_sequence):
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
		if shift_len >= 2 and local == 1:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		elif shift_len < 2 and local == 0:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_shift_orderB(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		answer = None
		if state[-1] == 1:
			gamma_state = []
			for i in range(1, len(state) - 1):
				gamma_state.append(1-state[i])
			gamma_state += [0, state[1]]
			answer = (gamma_state == find_conk(gamma_state))
		elif state[-1] == 0:
			local = shift_order([0] + state[1:])[0]
			answer = (local == 0)
			
		if answer is True:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
		
	return retval


def alg_shift_orderC(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		answer = None
		if state[-1] == 1:
			gamma_state = []
			for i in range(1, len(state) - 1):
				gamma_state.append(1 - state[i])
			gamma_state += [0, state[1]]
			answer = (gamma_state == find_conk(gamma_state))
		elif state[-1] == 0:
			change_state = [0] + state[1:]
			local, shift_len = shift_order(change_state)
			lens = shift_len % 4
			if lens == 0:
				lens = 4
			answer = local == lens - 1
		
		if answer is True:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_shift_orderD(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		answer = None
		if state[1] == 0:
			next_state = state[1:] + [1]
			answer = next_state == find_conk(next_state)
		elif state[1] == 1:
			change_state = state[1:] + [1]
			local, shift_len = shift_order_for_1(change_state)
			lens = shift_len % 4
			if lens == 0:
				lens = 4
			answer = local == lens - 1
		
		if answer is True:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


for n in range(6, 7):
	start = [0] * n
	s = ''.join([str(x) for x in alg_nkorrnk_D2(start)])
	s += s
	idx = s.find('0' * len(start))
	print(s[idx:idx + 2 ** (len(start))])
	print(len(s))
	print(n)
	# print(check_out(n, s))
