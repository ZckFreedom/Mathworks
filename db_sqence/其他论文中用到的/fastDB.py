from itertools import combinations


def Psr_sum(sequence):
	bit_sum = 0
	for i in range(1, len(sequence)):
		bit_sum += sequence[i]
	return bit_sum


def max_run_lengthZero(sequence):  #必须输入n+1长的necklace
	run_length = 0
	for i in range(len(sequence)):
		if sequence[i] == 1:
			return run_length
		run_length += 1


def find_nk(s_sequence):        #主要用在psr中，求n+1长的necklace，之后才能求最大0游程
	size = len(s_sequence)
	state = s_sequence[:]
	state += state
	states = []
	
	for i in range(0, size):
		if state[i: i + size] not in states:
			states.append(state[i: i + size])
	
	states.sort()
	return states[0]


def number_zero(sequence):
	size = len(sequence)
	zero_number = 0
	for i in range(size):
		if sequence[i] == 0:
			zero_number += 1
	return zero_number


def number_one(sequence):
	size = len(sequence)
	one_number = 0
	for i in range(size):
		if sequence[i] == 1:
			one_number += 1
	return one_number


def if_nk(sequence):
	period = 1
	size = len(sequence)
	for i in range(1, size):
		if sequence[i] > sequence[i-period]:
			period = i+1
		elif sequence[i] < sequence[i-period]:
			return False
	return size % period == 0


def shift_firstZero(sequence, ki):
	size = len(sequence)
	state = sequence[:]
	state += state
	local = 0
	shift_order = 0
	
	while shift_order < ki:
		local = local + 1
		if state[local] == 0:
			shift_order += 1
	
	return if_nk(state[local:local + size])


def shift_lastOne(sequence, ki):
	size = len(sequence)
	state = sequence[:]
	state += state
	local = size - 1
	shift_order = 0
	
	while shift_order < ki:
		local = local + 1
		if state[local] == 1:
			shift_order += 1
	
	return if_nk(state[local + 1 - size:local + 1])


def shift_runZero(sequence, shift_order):        #输入的时候输入n+1长的状态,直接输出是否满足条件A
	size = len(sequence)
	nk = find_nk(sequence)
	state = sequence[:]
	state += state
	max_runzero = max_run_lengthZero(nk)
	if max_run_lengthZero(sequence) != max_runzero:
		return False
	local = 0
	shift_number = 0
	
	while shift_number < shift_order:
		local = (local + 1) % size
		if max_run_lengthZero(state[local:local + size]) == max_runzero:
			shift_number += 1
	
	return if_nk(state[local:local + size])


def shift_lastOnePsr(sequence, ki):     #输入n+1长的状态，直接输出是否满足条件A
	size = len(sequence)
	state = sequence[:]
	state *= 20
	local = size - 1
	shift_order = 0
	next_one = None
	
	while shift_order < ki:
		local = local + 1
		if state[local] == 1:
			shift_order += 1
			if shift_order == 1:
				next_one = state[local + 1 - size:local + 1]
	lkv_state = state[local + 1 - size:local + 1]
	if lkv_state == sequence:
		return if_nk(next_one)
	else:
		return if_nk(lkv_state)


def lagest_one(sequence):
	size = len(sequence)
	state = sequence[:]
	state += state
	local = 2*size - 1
	shift_order = 0
	while shift_order < 1:
		local -= 1
		if state[local] == 1:
			shift_order += 1
	return if_nk(state[local + 1 - size:local + 1])


def smallest_one(sequence):
	size = len(sequence)
	state = sequence[:]
	state += state
	local = size - 1
	shift_order = 0
	while shift_order < 1:
		local += 1
		if state[local] == 1:
			shift_order += 1
	return if_nk(state[local + 1 - size:local + 1])


def alg_propositionSix_A(s_sequence, t_numbers):
	state = None
	retval = []
	number_len = len(t_numbers)
	number_list = [1]
	for i in range(0, number_len):
		number_list.append(t_numbers[i])
	number_list += [len(s_sequence), len(s_sequence)+1]
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		answer = None
		v_state = [0] + state[1:]
		zero_of_v = number_zero(v_state)
		for i in range(0, len(number_list) - 1):
			if number_list[i] <= zero_of_v < number_list[i + 1]:
				answer = shift_firstZero(v_state, number_list[i])
		
		if answer is True:
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def alg_propositionSix_B(s_sequence, t_numbers):
	state = None
	retval = []
	number_len = len(t_numbers)
	number_list = [1]
	for i in range(0, number_len):
		number_list.append(t_numbers[i])
	number_list += [len(s_sequence), len(s_sequence) + 1]
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		answer = None
		v_state = state[1:] + [1]
		one_of_v = number_one(v_state)
		for i in range(0, len(number_list) - 1):
			if number_list[i] <= one_of_v < number_list[i + 1]:
				answer = shift_lastOne(v_state, number_list[i]-1)
		
		if answer is True:
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def alg_propositionSeven_A(s_sequence, k_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		v_state = [0] + state[1:]
		zero_of_v = number_zero(v_state)
		answer = shift_firstZero(v_state, k_number % zero_of_v)
		
		if answer is True:
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def alg_propositionSeven_B(s_sequence, k_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		v_state = state[1:] + [1]
		one_of_v = number_one(v_state)
		answer = shift_lastOne(v_state, k_number % one_of_v)
		
		if answer is True:
			state = state[1:] + [1 - state[0]]
		else:
			state = state[1:] + [state[0]]
		
		retval.append(state[-1])
	
	return retval


def alg_propositionFourteen(s_sequence, k_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		v_state = state[1:] + [(1 + Psr_sum(state)) % 2, 1]
		answer = shift_runZero(v_state, k_number)
		
		if answer is True:
			state = state[1:] + [(Psr_sum(state) + state[0] + 1) % 2]
		else:
			state = state[1:] + [(Psr_sum(state) + state[0]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_propositionSeventeen(s_sequence, k_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		v_state = [(1 + Psr_sum(state)) % 2] + state[1:] + [1]
		answer = shift_lastOnePsr(v_state, k_number)
		
		if answer is True:
			state = state[1:] + [(Psr_sum(state) + state[0] + 1) % 2]
		else:
			state = state[1:] + [(Psr_sum(state) + state[0]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_lagest_one(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		v_state = [(1 + Psr_sum(state)) % 2] + state[1:] + [1]
		answer = lagest_one(v_state)
		
		if answer is True:
			state = state[1:] + [(Psr_sum(state) + state[0] + 1) % 2]
		else:
			state = state[1:] + [(Psr_sum(state) + state[0]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_smallest_one(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		v_state = [(1 + Psr_sum(state)) % 2] + state[1:] + [1]
		answer = smallest_one(v_state)
		
		if answer is True:
			state = state[1:] + [(Psr_sum(state) + state[0] + 1) % 2]
		else:
			state = state[1:] + [(Psr_sum(state) + state[0]) % 2]
		
		retval.append(state[-1])
	
	return retval


# start = [0] * 6
# store = []
# db_sequences = []
# for u in range(2, 6):
# 	store.append(u)
# for t in range(0, 6):
# 	all_ki = list(combinations(store, t))
# 	for k in range(0, len(all_ki)):
# 		s = ''.join([str(x) for x in alg_propositionSix_A(start, all_ki[k])])
# 		s += s
# 		idx = s.find('0' * len(start))
# 		ks = [1]
# 		if len(all_ki[k]) > 0:
# 			for num in range(len(all_ki[k])):
# 				ks += [all_ki[k][num]]
# 		ks += [6, 7]
# 		if s[idx:idx + 2 ** (len(start))] not in db_sequences:
# 			db_sequences.append(s[idx:idx + 2 ** (len(start))])
# 			print(ks, s[idx:idx + 2 ** (len(start))])
# for t in range(1, 20):
# 	s = ''.join([str(x) for x in alg_propositionSeventeen(start, t)])
# 	s += s
# 	idx = s.find('0' * len(start))
# 	if s[idx:idx + 2 ** (len(start))] not in db_sequences:
# 		db_sequences.append(s[idx:idx + 2 ** (len(start))])
# 		print('k='+str(t), s[idx:idx + 2 ** (len(start))])
# s = ''.join([str(x) for x in alg_lagest_one(start)])
# s += s
# idx = s.find('0' * len(start))
# if s[idx:idx + 2 ** (len(start))] not in db_sequences:
# 	db_sequences.append(s[idx:idx + 2 ** (len(start))])
# 	print(s[idx:idx + 2 ** (len(start))])
# s = ''.join([str(x) for x in alg_smallest_one(start)])
# s += s
# idx = s.find('0' * len(start))
# if s[idx:idx + 2 ** (len(start))] not in db_sequences:
# 	db_sequences.append(s[idx:idx + 2 ** (len(start))])
# 	print(s[idx:idx + 2 ** (len(start))])
