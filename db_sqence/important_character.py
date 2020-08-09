from Polynomials_Field import PolynomialsField


def xor(s1, s2):
	n = len(s1)
	b = ''
	for i in range(0, n):
		if s1[i] == s2[i]:
			b += '0'
		else:
			b += '1'
	return b


def games_chan(db):
	"""
	求db序列的线性复杂度
	"""
	sequence = db
	f = PolynomialsField([1], 2)
	n = len(sequence)
	liner_span = 0
	b = ''
	while n > 1:
		left, right = sequence[:int(n/2)], sequence[int(n/2):]
		b = xor(left, right)
		if b == '0' * int(n/2):
			sequence = left
		else:
			if n == 2:
				liner_span += 2
				f = f * (PolynomialsField([1, 1], 2) ** 2)
			else:
				liner_span += int(n / 2)
				f = f * (PolynomialsField([1, 1], 2) ** int(n/2))
			sequence = b
		n = int(n/2)
	if b == '0' * len(b):
		return liner_span + 1
	else:
		return liner_span


def find_n0(s1):
	for i in range(len(s1)):
		if int(s1[i]) == 1:
			return i


def find_m(lc_list):
	ln = lc_list[-1]
	for i in range(len(lc_list)-1, -1, -1):
		if lc_list[i] != ln:
			return i


def ply_add(l1, l2):
	a = len(l1)
	b = len(l2)
	add_ply = []
	if a > b:
		c = a-b
		l3 = [0]*c
		l3 += l2
		for i in range(a):
			add_ply.append((l1[i] + l3[i]) % 2)
	elif a < b:
		c = b-a
		l3 = [0] * c
		l3 += l1
		for i in range(b):
			add_ply.append((l1[i] + l3[i]) % 2)
	else:
		for i in range(b):
			add_ply.append((l1[i] + l2[i]) % 2)
	if add_ply[0] == 0:
		add_ply.pop(0)
	return add_ply


def b_m(sequence):
	"""
	求一般序列线性复杂度的BM算法
	"""
	N = len(sequence)
	mpl = []
	lcl = []
	n = find_n0(sequence)
	mp = [1]
	mp += [0]*int(n)
	mp += [1]
	for i in range(n):
		mpl.append([1])
		lcl.append(0)
	mpl.append(mp.copy())
	lcl.append(n+1)
	while n < N-1:
		n += 1
		d = 0
		for i in range(len(mp)):
			d += mp[i] * int(sequence[n-i])
		if d % 2 == 0:
			mpl.append(mpl[-1].copy())
			lcl.append(lcl[-1])
		elif d % 2 == 1:
			m_1_index = find_m(lcl)
			if m_1_index == 0:
				k = 1-n+lcl[-1]
			else:
				k = m_1_index+1-lcl[m_1_index]-n+lcl[-1]
			if k >= 0:
				mpm = mpl[m_1_index] + [0]*k
				mp = ply_add(mp, mpm)
				mpl.append(mp.copy())
				lcl.append(lcl[-1])
			elif k < 0:
				mp += [0] * int(-k)
				mp = ply_add(mp, mpl[m_1_index])
				mpl.append(mp.copy())
				lcl.append(n+1-lcl[-1])
	return mpl[-1], lcl[-1]


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


def prr_cycles(k, n):
	cycle_list = []
	middle_list = []
	mark_number = 0
	for s_sequence in generator_of_all_sequences(k, n):
		for mark in range(0, len(cycle_list)):
			if s_sequence in cycle_list[mark]:
				mark_number = 1
		if mark_number == 0:
			middle_list.append(s_sequence.copy())
			state = s_sequence[1:] + [(s_sequence[1] + s_sequence[0] + s_sequence[-1]) % k]
			while state != s_sequence:
				middle_list.append(state)
				state = state[1:] + [(state[1] + state[0] + state[-1]) % k]
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


cycle = prr_cycles(2, 6)
for i in range(len(cycle)):
	print(cycle[i])
