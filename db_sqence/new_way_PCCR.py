from itertools import combinations


def find_nk(s_sequence):
	size = len(s_sequence)
	state = s_sequence[:size - 1]
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
	for i in range(size - 1, -1, -1):
		if states.if_not_in(necklace[i:i + size + 1]) and necklace[i] == 1:
			states.append(necklace[i:i + size + 1])
	
	return states.find_sequence(s_sequence), states.len()


def alg_A(s_sequence, t_numbers):
	state = None
	retval = []
	number_len = len(t_numbers)
	number_list = [1]
	for i in range(0, number_len):
		number_list.append(t_numbers[i])
	number_list.append(len(s_sequence)-1)
	
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
			if number_len == 0:
				answer = (local == t_numbers[0] - 1 and shift_len >= t_numbers[0]) or (local == 0 and shift_len < t_numbers[0])
			else:
				for i in range(0, len(number_list) - 1):
					if number_list[i] <= shift_len < number_list[i + 1] and local == number_list[i] - 1:
						answer = True
	
		if answer is True:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_C(s_sequence, t_numbers):
	state = None
	retval = []
	number_len = len(t_numbers)
	number_list = [1]
	for i in range(0, number_len):
		number_list.append(t_numbers[i])
	number_list.append(len(s_sequence) - 1)
	
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
			if number_len == 0:
				answer = (local == t_numbers[0] - 1 and shift_len >= t_numbers[0]) or (local == 0 and shift_len < t_numbers[0])
			else:
				for i in range(0, len(number_list) - 1):
					if number_list[i] <= shift_len < number_list[i + 1] and local == number_list[i] - 1:
						answer = True
		
		if answer is True:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_A1(s_sequence, k_number):
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
			if local == k_number % shift_len:
				answer = True
		
		if answer is True:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_C1(s_sequence, k_number):
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
			if local == k_number % shift_len:
				answer = True
		
		if answer is True:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


start = [0] * 6
store = [2, 3, 4]
db_sequences = []
# for t in range(1, 5):
# 	all_ki = list(combinations(store, t))
# 	for k in range(0, len(all_ki)):
# 		s = ''.join([str(x) for x in alg_C(start, all_ki[k])])
# 		s += s
# 		idx = s.find('0' * len(start))
# 		if s[idx:idx + 2 ** (len(start))] not in db_sequences:
# 			db_sequences.append(s[idx:idx + 2 ** (len(start))])
# 			print(all_ki[k], s[idx:idx + 2 ** (len(start))])
for t in range(1, 13):
	s = ''.join([str(x) for x in alg_C1(start, t)])
	s += s
	idx = s.find('0' * len(start))
	if s[idx:idx + 2 ** (len(start))] not in db_sequences:
		db_sequences.append(s[idx:idx + 2 ** (len(start))])
		print('k='+str(t), '&'+s[idx:idx + 2 ** (len(start))])
