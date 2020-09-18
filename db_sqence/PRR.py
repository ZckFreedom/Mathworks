from itertools import combinations


def hamming_weight(a_sequence):     #输入一个cycle列表，输出其汉明重量
	weight = 0
	for j in range(len(a_sequence)):
		if a_sequence[j] == 1:
			weight += 1
	return weight


def numberZero(a_sequence):
	zeronumber = 0
	for j in range(len(a_sequence)):
		if a_sequence[j] == 0:
			zeronumber += 1
	return zeronumber


def if_nk(sequence):    #输入n-1长的序列，判断是否是necklace
	period = 1
	size = len(sequence)
	for i in range(1, size):
		if sequence[i] > sequence[i-period]:
			period = i+1
		elif sequence[i] < sequence[i-period]:
			return False
	return size % period == 0


def if_conk(sequence):     #输入n-1长的序列，判断是否是co-necklace
	state = sequence[:]
	state += [1 - x for x in state]
	return if_nk(state)


def shift_lastOne(sequence, ki):        #输入n-1长的序列W和ki-1,输出L1对W作用ki-1次是否是necklace
	size = len(sequence)
	state = sequence[:]
	state += state
	shift_order = 0
	local = size - 1
	
	while shift_order < ki:
		local += 1
		if state[local] == 1:
			shift_order += 1
			
	return if_nk(state[local + 1 - size:local + 1])


def shift_firstZero(sequence, ki):  #输入n-1长的序列W和ki-1,输出F0对W作用ki-1次是否是necklace
	size = len(sequence)
	state = sequence[:]
	state += state
	shift_order = 0
	local = 0
	
	while shift_order < ki:
		local = local + 1
		if state[local] == 0:
			shift_order += 1
	
	return if_nk(state[local:local + size])


def alg_propositionSeven(s_sequence, t_numbers):
	state = None
	retval = []
	number_list = [1]
	for i in range(len(t_numbers)):
		number_list.append(t_numbers[i])
	number_list += [len(s_sequence)]
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		answer = None
		u_state = [0] + state[2:]
		w_state = state[2:] + [1]
		if state[1] == 0:
			answer = if_conk(u_state)
		else:
			weight = hamming_weight(w_state)
			for i in range(0, len(number_list) - 1):
				if number_list[i] <= weight < number_list[i + 1]:
					answer = shift_lastOne(w_state, number_list[i]-1)
		
		if answer:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_propositionNine(s_sequence, k_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]

		u_state = [0] + state[2:]
		w_state = state[2:] + [1]
		if state[1] == 0:
			answer = if_conk(u_state)
		else:
			answer = shift_lastOne(w_state, k_number % hamming_weight(w_state))
		
		if answer:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_propositionTwelve(s_sequence, t_numbers):
	state = None
	retval = []
	number_list = [1]
	for i in range(len(t_numbers)):
		number_list.append(t_numbers[i])
	number_list += [len(s_sequence)]
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		answer = None
		u_state = [1 - bit for bit in state[1:]]
		w_state = [0] + state[1:len(state) - 1]
		if state[-1] == 1:
			answer = if_conk(u_state)
		else:
			for i in range(0, len(number_list) - 1):
				if number_list[i] <= numberZero(w_state) < number_list[i + 1]:
					answer = shift_firstZero(w_state, number_list[i] - 1)
		
		if answer:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_propositionThirteen(s_sequence, k_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		u_state = [1 - bit for bit in state[1:]]
		w_state = [0] + state[1:len(state) - 1]
		if state[-1] == 1:
			answer = if_conk(u_state)
		else:
			answer = shift_firstZero(w_state, k_number % numberZero(w_state))
		
		if answer:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


start = [0] * 6
store = [2, 3, 4, 5]
db_sequences = []
for t in range(0, 4):
	all_ki = list(combinations(store, t))
	for k in range(0, len(all_ki)):
		s = ''.join([str(x) for x in alg_propositionTwelve(start, all_ki[k])])
		s += s
		idx = s.find('0' * len(start))
		ks = [1]
		if len(all_ki[k]) > 0:
			for num in range(len(all_ki[k])):
				ks += [all_ki[k][num]]
		ks += [6]
		if s[idx:idx + 2 ** (len(start))] not in db_sequences:
			db_sequences.append(s[idx:idx + 2 ** (len(start))])
			print(ks, s[idx:idx + 2 ** (len(start))])
# for t in range(20):
# 	s = ''.join([str(x) for x in alg_propositionNine(start, t)])
# 	s += s
# 	idx = s.find('0' * len(start))
# 	if s[idx:idx + 2 ** (len(start))] not in db_sequences:
# 		db_sequences.append(s[idx:idx + 2 ** (len(start))])
# 		print('k='+str(t), s[idx:idx + 2 ** (len(start))])
