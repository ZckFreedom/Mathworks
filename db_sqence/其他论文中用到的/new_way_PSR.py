from interval import Interval
from itertools import combinations
from check_out import check_out


def Psr_list(s_sequence):
	size = len(s_sequence)
	sums = 0
	
	for i in range(1, size):
		sums = (sums + s_sequence[i]) % 2
	return sums


def max_run_of0(s_sequence):
	cnt = 0
	counter = []
	
	for i in range(0, len(s_sequence)):
		if s_sequence[i] == 1:
			counter.append(cnt)
			cnt = 0
		elif s_sequence[i] == 0:
			cnt += 1
	counter.append(cnt)
	
	counter.sort()
	return counter[-1]


def find_nk(s_sequence):
	size = len(s_sequence)
	state = s_sequence[:]
	state += state
	states = []
	
	for i in range(0, size):
		if state[i: i + size] not in states:
			states.append(state[i: i + size])
	
	states.sort()
	return states[0]


def shift_order_psr(s_sequence):
	size = len(s_sequence)
	nk = find_nk(s_sequence + [(Psr_list(s_sequence) + s_sequence[0]) % 2])
	nk += nk
	
	left_shift = Shift_order_space()
	
	for i in range(0, size):
		if left_shift.check(nk[i:i + size]):
			left_shift.append(nk[i:i + size])
	
	return left_shift.get_number(s_sequence), left_shift.get_len()


class Shift_order_space:
	def __init__(self):
		self._shiftlist = []
		self._shiftnumber = 0
	
	def get_number(self, a_list):
		for i in range(0, len(self._shiftlist)):
			if a_list == self._shiftlist[i][0]:
				return self._shiftlist[i][1]
		return -1
	
	def get_len(self):
		return self._shiftnumber
	
	def append(self, a_list):
		self._shiftnumber += 1
		self._shiftlist.append((a_list, self._shiftnumber))
	
	def if_not_in(self, a_list):
		if len(self._shiftlist) == 0:
			return True
		for i in range(0, len(self._shiftlist)):
			if self._shiftlist[i][0] == a_list:
				return False
		return True
	
	def check(self, a_list):
		if self.if_not_in(a_list) is not True:
			return False
		return a_list[0] == 1 and Psr_list(a_list) == 0


class Run_shift_order:
	def __init__(self, max_run):
		self._shiftlist = []
		self._shiftnumber = 0
		self._run = max_run
	
	def get_number(self, a_list):
		for i in range(0, len(self._shiftlist)):
			if a_list == self._shiftlist[i][0]:
				return self._shiftlist[i][1]
		return -1
	
	def get_len(self):
		return self._shiftnumber
	
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
	
	def check(self, a_list):
		if self.if_not_in(a_list) is not True:
			return False
		cnt = 0
		for i in a_list[1:]:
			if i == 0:
				cnt += 1
			else:
				break
		return cnt == self._run


def shift_run_number(s_sequence):
	size = len(s_sequence)
	nk = find_nk(s_sequence)
	max_run = max_run_of0(nk)
	nk += nk
	max_run_states = Run_shift_order(max_run)
	
	for i in range(size - 1, 0, -1):
		if max_run_states.check(nk[i:i + size]):
			max_run_states.append(nk[i:i + size])
	
	return max_run_states.get_number(s_sequence), max_run_states.get_len()


def alg_run_orderA(s_sequence, k_numbers):  # F1
	state = None
	retval = []
	number_len = len(k_numbers)
	len_state = len(s_sequence)
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		local, m = shift_run_number([1] + state[1:] + [1 - Psr_list(state)])
		next_state = state[1:] + [1 - Psr_list(state)] + [1]
		if number_len == 1:
			if m >= k_numbers[0] and local == k_numbers[0] - 1 or m < k_numbers[0] and next_state == find_nk(next_state):
				state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
			else:
				state = state[1:] + [(Psr_list(state) + state[0]) % 2]
		
			retval.append(state[-1])
		else:
			answer = None
			number_list = [1]
			for i in range(0, number_len):
				number_list.append(k_numbers[i])
			number_list.append(len_state)
			for i in range(1, len(number_list) - 1):
				if number_list[i] <= m < number_list[i + 1] and local == number_list[i] - 1:
					answer = True
				if m < number_list[1] and next_state == find_nk(next_state):
					answer = True
			if answer:
				state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
			else:
				state = state[1:] + [(Psr_list(state) + state[0]) % 2]
			
			retval.append(state[-1])
			
	return retval


def alg_run_orderB(s_sequence, t_number):  # F2
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		local, m = shift_run_number([1] + state[1:] + [1 - Psr_list(state)])
		next_state = state[1:] + [1 - Psr_list(state)] + [1]
		lens = m % t_number
		if lens == 0:
			lens = t_number
		if local == lens - 1:
			state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
		else:
			state = state[1:] + [(Psr_list(state) + state[0]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_shift_orderA(s_sequence, k_numbers):  # G1
	state = None
	retval = []
	number_len = len(k_numbers)
	len_state = len(s_sequence)
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		local, m = shift_order_psr([1] + state[1:])
		next_state = state[1:] + [1 - Psr_list(state)] + [1]
		if number_len == 1:
			if m >= k_numbers[0] and local == k_numbers[0] or m < k_numbers[0] and next_state == find_nk(next_state):
				state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
			else:
				state = state[1:] + [(Psr_list(state) + state[0]) % 2]
		
			retval.append(state[-1])
		else:
			answer = None
			number_list = [1]
			for i in range(0, number_len):
				number_list.append(k_numbers[i])
			number_list.append(len_state)
			for i in range(1, len(number_list) - 1):
				if number_list[i] <= m < number_list[i + 1] and local == number_list[i] - 1:
					answer = True
				if m < number_list[1] and next_state == find_nk(next_state):
					answer = True
			if answer:
				state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
			else:
				state = state[1:] + [(Psr_list(state) + state[0]) % 2]
			
			retval.append(state[-1])
	
	return retval


def alg_shift_orderB(s_sequence, k_number):  # G2
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		local, m = shift_order_psr([1] + state[1:])
		next_state = state[1:] + [1 - Psr_list(state)] + [1]
		lens = m % k_number
		if lens == 0:
			lens = k_number
		if (m == 0 and next_state == find_nk(next_state)) or local == lens:
			state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
		else:
			state = state[1:] + [(Psr_list(state) + state[0]) % 2]
		
		retval.append(state[-1])
	
	return retval


start = [0] * 6
store = [2, 3, 4, 5]
db_sequences = []
for t in range(1, 5):
	all_ki = list(combinations(store, t))
	for k in range(0, len(all_ki)):
		s = ''.join([str(x) for x in alg_run_orderA(start, all_ki[k])])
		s += s
		idx = s.find('0' * len(start))
		if s[idx:idx + 2 ** (len(start))] not in db_sequences:
			db_sequences.append(s[idx:idx + 2 ** (len(start))])
			print(all_ki[k], s[idx:idx + 2 ** (len(start))])
			# print(check_out(6, s))
# for t in range(2, 6):
# 	s = ''.join([str(x) for x in alg_shift_orderB(start, t)])
# 	s += s
# 	idx = s.find('0' * len(start))
# 	if s[idx:idx + 2 ** (len(start))] not in db_sequences:
# 		db_sequences.append(s[idx:idx + 2 ** (len(start))])
# 		print(t, s[idx:idx + 2 ** (len(start))])
		# print(check_out(6, s))
