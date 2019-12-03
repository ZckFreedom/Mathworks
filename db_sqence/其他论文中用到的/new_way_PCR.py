from interval import Interval
from itertools import combinations
from check_out import check_out


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


def shift_order_last1(s_sequence):
	size = len(s_sequence)
	s_sequence += s_sequence
	
	real_states = Shift_order_space()
	for i in range(size, -1, -1):
		if real_states.if_not_in(s_sequence[i:i + size]) and s_sequence[i + size - 1] == 1:
			real_states.append((s_sequence[i:i + size]))
	
	real_states.select_sort()
	return real_states.get_number(), real_states.len()


def shift_order_alg_A(s_sequence, t_numbers):  # D1
	state = None
	retval = []
	number_len = len(t_numbers)
	len_state = len(s_sequence)
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		kk, m = shift_order_first0([0] + state[1:])
		if number_len == 1:
			if (kk == t_numbers[0] - 1 and m >= t_numbers[0]) or (kk == 0 and m < t_numbers[0]):
				state = state[1:] + [1 - state[0]]
			else:
				state = state[1:] + [state[0]]
			
			retval.append(state[-1])
		else:
			answer = None
			number_list = [1]
			for i in range(0, number_len):
				number_list.append(t_numbers[i])
			number_list.append(len_state)
			for i in range(0, len(number_list) - 1):
				if number_list[i] <= m < number_list[i + 1] and kk == number_list[i] - 1:
					answer = True
			if answer:
				state = state[1:] + [1 - state[0]]
			else:
				state = state[1:] + [state[0]]
			
			retval.append(state[-1])
	
	return retval


def shift_order_alg_B(s_sequence, t_number):  # D2
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		kk, m = shift_order_first0([0] + state[1:])
		lens = m % t_number
		if lens == 0:
			lens = t_number
		if kk == lens - 1:
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def shift_order_alg_C(s_sequence, t_numbers):  # E1
	state = None
	retval = []
	number_len = len(t_numbers)
	len_state = len(s_sequence)
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		kk, m = shift_order_last1(state[1:] + [1])
		if number_len == 1:
			if (kk == t_numbers[0] - 1 and m >= t_numbers[0]) or (kk == 0 and m < t_numbers[0]):
				state = state[1:] + [1 - state[0]]
			else:
				state = state[1:] + [state[0]]
			
			retval.append(state[-1])
		else:
			answer = None
			number_list = [1]
			for i in range(0, number_len):
				number_list.append(t_numbers[i])
			number_list.append(len_state)
			for i in range(0, len(number_list) - 1):
				if number_list[i] <= m < number_list[i + 1] and kk == number_list[i] - 1:
					answer = True
			if answer:
				state = state[1:] + [1 - state[0]]
			else:
				state = state[1:] + [state[0]]
			
			retval.append(state[-1])
	
	return retval


def shift_order_alg_D(s_sequence, t_number):  # E2
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		kk, m = shift_order_last1(state[1:] + [1])
		lens = m % t_number
		if lens == 0:
			lens = t_number
		if kk == lens - 1:
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


start = [0] * 6
store = [2, 3, 4, 5]
db_sequences = []
# for t in range(1, 5):
# 	all_ki = list(combinations(store, t))
# 	for k in range(0, len(all_ki)):
# 		s = ''.join([str(x) for x in shift_order_alg_C(start, all_ki[k])])
# 		s += s
# 		idx = s.find('0' * len(start))
# 		if s[idx:idx + 2 ** (len(start))] not in db_sequences:
# 			db_sequences.append(s[idx:idx + 2 ** (len(start))])
# 			print(all_ki[k], s[idx:idx + 2 ** (len(start))])
# 			# print(check_out(6, s))
for t in range(2, 6):
	s = ''.join([str(x) for x in shift_order_alg_D(start, t)])
	s += s
	idx = s.find('0' * len(start))
	if s[idx:idx + 2 ** (len(start))] not in db_sequences:
		db_sequences.append(s[idx:idx + 2 ** (len(start))])
		print(t, s[idx:idx + 2 ** (len(start))])
		# print(check_out(6, s))
