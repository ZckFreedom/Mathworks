import time

start_time = time.perf_counter()


def generator_of_all_sequences(k, sequence_order):
	cnt = 0
	sequence = [0] * sequence_order
	while cnt < k**sequence_order:
		for bit in range(0, sequence_order):
			bit_number = cnt // (k ** (sequence_order - 1 - bit))
			sequence[bit] = bit_number % k
		cnt += 1
		yield sequence


def check_out(ary, sequence_order, s_sequence):
	not_such = []
	for state in generator_of_all_sequences(ary, sequence_order):
		se = ''.join([str(x) for x in state])
		if s_sequence.find(se) == -1:
			not_such.append(se)
			# print('it is not a dB_sequence!')
	if len(not_such) == 0:
		return 1
	else:
		return not_such


def if_nk(s_sequence):
	size = len(s_sequence)
	s = s_sequence[:]
	s += s
	states = []
	
	for i in range(0, size):
		if s[i: i + size] not in states:
			states.append(s[i: i + size])
	
	states.sort()
	return s_sequence == states[0]


def pcr_cycles(k, n):
	cycle_list = []
	middle_list = []
	mark_number = 0
	for s_sequence in generator_of_all_sequences(k, n):
		for mark in range(0, len(cycle_list)):
			if s_sequence in cycle_list[mark]:
				mark_number = 1
		if mark_number == 0:
			middle_list.append(s_sequence.copy())
			state = s_sequence[1:] + [s_sequence[0]]
			while state != s_sequence:
				middle_list.append(state)
				state = state[1:] + [state[0]]
			cycle_list.append(middle_list.copy())
			middle_list.clear()
		mark_number = 0
	return cycle_list


def ccr_cycles(k, n):
	cycle_list = []
	middle_list = []
	mark_number = 0
	for s_sequence in generator_of_all_sequences(k, n):
		for mark in range(0, len(cycle_list)):
			if s_sequence in cycle_list[mark]:
				mark_number = 1
		if mark_number == 0:
			middle_list.append(s_sequence.copy())
			state = s_sequence[1:] + [(1 + s_sequence[0]) % k]
			while state != s_sequence:
				middle_list.append(state)
				state = state[1:] + [(1 + state[0]) % k]
			cycle_list.append(middle_list.copy())
			middle_list.clear()
		mark_number = 0
	return cycle_list


def pcr_cycles_joint_step1(k, n):
	cycle_list = []
	middle_list = ''
	mark_number = 0
	for s_sequence in generator_of_all_sequences(k, n):
		for mark in range(0, len(cycle_list)):
			if ''.join([str(x) for x in s_sequence]) in cycle_list[mark]:
				mark_number = 1
		if mark_number == 0:
			x_max = 0
			middle_list += '-->' + ''.join([str(x) for x in s_sequence.copy()])
			middle_sequence = [s_sequence[0] + 1] + s_sequence[1:]
			while if_nk(middle_sequence) is True:
				x_max += 1
				middle_sequence = [middle_sequence[0] + 1] + middle_sequence[1:]
			middle_sequence.clear()
			if x_max == 0:
				state = s_sequence[1:] + [s_sequence[0]]
			else:
				state = s_sequence[1:] + [s_sequence[0] + 1]
			while state != s_sequence:
				middle_list += '-->' + ''.join([str(x) for x in state])
				if if_nk(state) and state[0] < x_max:
					state = state[1:] + [state[0] + 1]
				elif if_nk(state) and state[0] == x_max:
					state = state[1:] + [0]
				else:
					state = state[1:] + [state[0]]
			cycle_list.append(middle_list)
			middle_list = ''
		mark_number = 0
	return cycle_list


# a = pcr_cycles(3, 4)
# print(a)


def find_max_x(s_sequence, k):
	x_max = k - 1
	middle_sequence = s_sequence[1:] + [x_max]
	while if_nk(middle_sequence) is not True and x_max > -1:
		x_max -= 1
		middle_sequence = s_sequence[1:] + [x_max]
	
	return x_max


def find_first_max(s_sequence, k):
	x_max = k - 2
	middle_sequence = [x_max] + s_sequence[1:]
	while x_max > -1:
		if if_nk(middle_sequence):
			return x_max
		else:
			x_max -= 1
			middle_sequence = [x_max] + s_sequence[1:]
	
	return -1


def find_min_x(s_sequence, k):
	x_min = 1
	middle_sequence = s_sequence[1:] + [x_min]
	while if_nk(middle_sequence) is not True and x_min < k:
		x_min += 1
		middle_sequence = s_sequence[1:] + [x_min]
	
	if x_min < k:
		return x_min
	else:
		return -1


def k_ary_dB1(s_sequence, k):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		conjugate_state = [state[0] + 1] + state[1:]
		next_state = state[1:] + [state[0]]
		next_sub_state = state[1:] + [state[0] - 1]
		
		if if_nk(state) and if_nk(conjugate_state) and conjugate_state[0] != k:
			state = state[1:] + [state[0] + 1]
		elif if_nk(state) and (not if_nk(conjugate_state) or conjugate_state[0] == k) and state[1] != 0:
				state = state[1:] + [0]
		elif state[0:2] == [0, 0]:
			x_max = find_max_x(state, k)
			if x_max != -1:
				state = state[1:] + [x_max]
			else:
				state = state[1:] + [state[0]]
		elif if_nk(next_state) and state[1] == 0 and state[0] > 0:
			if if_nk(next_sub_state):
				state = state[1:] + [state[0] - 1]
			else:
				state = state[1:] + [0]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])

	return retval


def k_ary_dB2(s_sequence, k):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		conjugate_state = [state[0] + 1] + state[1:]
		next_state = state[1:] + [state[0]]
		
		if if_nk(state) and if_nk(conjugate_state) and conjugate_state[0] != k:
			state = state[1:] + [state[0] + 1]
		elif if_nk(state) and (not if_nk(conjugate_state) or conjugate_state[0] == k) and state[1] != 0:
				state = state[1:] + [0]
		elif state[0:2] == [0, 0]:
			x_min = find_min_x(state, k)
			if x_min != -1:
				state = state[1:] + [x_min]
			else:
				state = state[1:] + [state[0]]
		elif if_nk(next_state) and state[1] == 0:
			if state[0] == k - 1:
				state = state[1:] + [0]
			else:
				state = state[1:] + [state[0] + 1]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
		
	return retval


def k_ary_dB3(s_sequence, k):
	"""
	论文中g1
	"""
	state = None
	retval = []

	while state != s_sequence:
		if state is None:
			state = s_sequence[:]

		x_max = find_first_max(state, k)

		if state[0] < x_max + 1 and x_max != -1:
			state = state[1:] + [state[0] + 1]
		elif state[0] == x_max + 1 and x_max != -1:
			state = state[1:] + [0]
		else:
			state = state[1:] + [state[0]]

		retval.append(state[-1])

	return retval


def k_ary_dB4(s_sequence, k):
	"""
	论文 中g1'
	"""
	state = None
	retval = []

	while state != s_sequence:
		if state is None:
			state = s_sequence[:]

		x_max = find_first_max(state, k)

		if 0 < state[0] <= x_max + 1 and x_max != -1:
			state = state[1:] + [state[0] - 1]
		elif state[0] == 0 and x_max != -1:
			state = state[1:] + [x_max + 1]
		else:
			state = state[1:] + [state[0]]

		retval.append(state[-1])

	return retval


start = [0] * 3
b = ''.join([str(x) for x in k_ary_dB4(start, 3)])
b += b
print(len(b))
idx = b.find('0' * len(start))
print(b[idx:idx + 3 ** 3])
# print(check_out(4, 11, b))
print(time.perf_counter() - start_time, "seconds")
