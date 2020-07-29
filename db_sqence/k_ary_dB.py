import time

start_time = time.perf_counter()


def if_nk(sequence_list, ary):
	if len(sequence_list) == 0:
		return False
	n = len(sequence_list)
	degree = ary ** (n-1)
	value1 = 0
	for i in range(n):
		value1 += sequence_list[i] * (ary ** (n-i-1))
	a1 = value1//degree
	value2 = (ary * value1 + a1) % (ary ** n)
	while value2 != value1:
		if value2 < value1:
			return False
		a1 = value2 // degree
		value2 = (ary * value2 + a1) % (ary ** n)
	return True


def find_first_max(s_sequence, ary):
	x_max = ary - 2
	middle_sequence = [x_max] + s_sequence[1:]
	while x_max > -1:
		if if_nk(middle_sequence, ary):
			return x_max
		else:
			x_max -= 1
			middle_sequence = [x_max] + s_sequence[1:]
	
	return -1


def r_set(sequence, ary):
	if sequence[0] + sequence[1] != 0:
		return []
	t = ary-1
	new_state = sequence[1:] + [t]
	r_list = []
	if not if_nk(new_state, ary):
		return []
	r_list.append(t)
	while t > 1:
		t = t-1
		new_state = sequence[1:] + [t]
		if if_nk(new_state, ary):
			r_list.append(t)
		else:
			r_list.reverse()
			return r_list
	r_list.reverse()
	return r_list


def g_set(sequence, ary):
	if sequence[0] != 0:
		return []
	t = ary - 1
	new_state = sequence[1:] + [t]
	r_list = []
	if not if_nk(new_state, ary):
		return []
	r_list.append(t)
	while t > 1:
		t = t - 1
		new_state = sequence[1:] + [t]
		if if_nk(new_state, ary):
			r_list.append(t)
		else:
			r_list.reverse()
			return r_list
	r_list.reverse()
	return r_list


def length_first0(sequence):
	length = 0
	for i in range(len(sequence)):
		if sequence[i] != 0:
			return length
		length += 1
	return length


def if_A0(sequence, ary):
	if sequence[1] != 0:
		return False
	next_state = sequence[1:] + [sequence[0]]
	if if_nk(next_state, ary):
		return True
	else:
		return False

	
def k_ary_h0(sequence, ary, j):     #论文中的H，不包括奇偶情况
	state = None
	retval = []
	
	while state != sequence:
		if state is None:
			state = sequence[:]
		
		if state[0] == ary-1:
			beta = []
		else:
			beta = [state[0] + 1] + state[1:]
		gamma = [0] + state[1:]
		Rset_alpha = r_set(state, ary)
		
		if len(Rset_alpha) != 0:
			state = state[1:] + [Rset_alpha[(j-1) % len(Rset_alpha)]]
		elif if_A0(state, ary):
			Rset = r_set(gamma, ary)
			if len(Rset) == 1:
				state = state[1:] + [0]
			else:
				if state[0] == Rset[(j-2) % len(Rset)]:
					state = state[1:] + [0]
				else:
					if state[0] == ary - 1:
						state = state[1:] + [Rset[0]]
					else:
						state = state[1:] + [(state[0] + 1) % ary]
		else:
			if if_nk(beta, ary):
				state = state[1:] + [(state[0] + 1) % ary]
			elif if_nk(state, ary) and state[1] != 0 and not if_nk(beta, ary):
				state = state[1:] + [0]
			else:
				state = state[1:] + [state[0]]
		retval.append(state[-1])
	return retval


def k_ary_h01(sequence, ary, j, k):  # 论文中的H，包括奇偶情况
	state = None
	retval = []
	
	while state != sequence:
		if state is None:
			state = sequence[:]
		
		if state[0] == ary - 1:
			beta = []
		else:
			beta = [state[0] + 1] + state[1:]
		gamma = [0] + state[1:]
		Rset_alpha = r_set(state, ary)
		
		if len(Rset_alpha) != 0:
			if length_first0(state) % 2 == 1:
				state = state[1:] + [Rset_alpha[(j - 1) % len(Rset_alpha)]]
			else:
				state = state[1:] + [Rset_alpha[(k - 1) % len(Rset_alpha)]]
		elif if_A0(state, ary):
			Rset = r_set(gamma, ary)
			zero_length = length_first0(gamma)
			if len(Rset) == 1:
				state = state[1:] + [0]
			else:
				if zero_length % 2 == 1 and state[0] == Rset[(j - 2) % len(Rset)]:
					state = state[1:] + [0]
				elif zero_length % 2 == 0 and state[0] == Rset[(k - 2) % len(Rset)]:
					state = state[1:] + [0]
				else:
					if state[0] == ary - 1:
						state = state[1:] + [Rset[0]]
					else:
						state = state[1:] + [(state[0] + 1) % ary]
		else:
			if if_nk(beta, ary):
				state = state[1:] + [(state[0] + 1) % ary]
			elif if_nk(state, ary) and state[1] != 0 and not if_nk(beta, ary):
				state = state[1:] + [0]
			else:
				state = state[1:] + [state[0]]
		retval.append(state[-1])
	return retval


def k_ary_g0(sequence, ary, j):  # 论文中的G，不包括奇偶情况
	state = None
	retval = []
	
	while state != sequence:
		if state is None:
			state = sequence[:]
		
		beta = state[1:] + [state[0]]
		gamma = [0] + state[1:]
		Rset_alpha = g_set(state, ary)
		
		if len(Rset_alpha) != 0:
			state = state[1:] + [Rset_alpha[(j - 1) % len(Rset_alpha)]]
		elif if_nk(beta, ary):
			Rset = g_set(gamma, ary)
			if len(Rset) == 1:
				state = state[1:] + [0]
			else:
				if state[0] == Rset[(j - 2) % len(Rset)]:
					state = state[1:] + [0]
				else:
					if state[0] == ary - 1:
						state = state[1:] + [Rset[0]]
					else:
						state = state[1:] + [(state[0] + 1) % ary]
		else:
			state = state[1:] + [state[0]]
		retval.append(state[-1])
	return retval


def k_ary_g01(sequence, ary, j, k):  # 论文中的G，包括奇偶情况
	state = None
	retval = []
	
	while state != sequence:
		if state is None:
			state = sequence[:]
		
		beta = state[1:] + [state[0]]
		gamma = [0] + state[1:]
		Rset_alpha = g_set(state, ary)
		
		if len(Rset_alpha) != 0:
			if length_first0(state) % 2 == 1:
				state = state[1:] + [Rset_alpha[(j - 1) % len(Rset_alpha)]]
			else:
				state = state[1:] + [Rset_alpha[(k - 1) % len(Rset_alpha)]]
		elif if_nk(beta, ary):
			Rset = g_set(gamma, ary)
			zero_length = length_first0(gamma)
			if len(Rset) == 1:
				state = state[1:] + [0]
			else:
				if zero_length % 2 == 1 and state[0] == Rset[(j - 2) % len(Rset)]:
					state = state[1:] + [0]
				elif zero_length % 2 == 0 and state[0] == Rset[(k - 2) % len(Rset)]:
					state = state[1:] + [0]
				else:
					if state[0] == ary - 1:
						state = state[1:] + [Rset[0]]
					else:
						state = state[1:] + [(state[0] + 1) % ary]
		else:
			state = state[1:] + [state[0]]
		retval.append(state[-1])
	return retval


def k_ary_g1(s_sequence, k):
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


def k_ary_g11(s_sequence, k):
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


start = [0] * 4
b = ''.join([str(x) for x in k_ary_g01(start, 3, 1, 2)])
b += b
# print(len(b))
idx = b.find('0' * len(start))
print(b[idx:idx + 3 ** 4])
# print(check_out(4, 11, b))
print(time.perf_counter() - start_time, "seconds")
