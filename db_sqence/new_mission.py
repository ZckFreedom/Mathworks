from dB_for_powers import generator_of_all_sequnces


# sequence_a = [0, 0, 0, 1, 1, 1, 0, 1]
# sequence_a = [0, 0, 1, 1]
sequence_a = [0, 1]


def cycles(n):
	all_sequence = []
	# all_cyeles = []
	# middle_cycle = []
	reveal = []
	
	# for sequences in generator_of_all_sequnces(n):
	# 	all_sequence.append(sequences[:])

	for sequence in generator_of_all_sequnces(n):
		cnt = 0
		state = None
		while state != sequence or cnt % 2 != 0:
			if state is None:
				state = sequence[:]
				# middle_cycle.append(state)
			reveal.append(state[-1])
			# state = state[1:] + [(state[0] + state[1] + state[3] + state[5] + sequence_a[cnt % 8]) % 2]
			state = state[1:] + [(state[0] + state[1] + state[4] + sequence_a[cnt % 2]) % 2]
			# state = state[1:] + [(state[0] + state[1] + state[2] + state[4] + state[5] + state[6] + state[8] + state[9] + sequence_a[cnt % 4]) % 2]
			cnt += 1
		yield reveal[:]
		reveal.clear()

	# 	all_cyeles.append(middle_cycle[:])
	# 	middle_cycle.clear()
	#
	# return all_cyeles


def is_one(c1, c2):
	if len(c1) != len(c2):
		return False
	cycle1 = ''.join([str(x) for x in c1])
	cycle2 = ''.join([str(x) for x in c2])
	cycle2 += cycle2
	if cycle2.find(cycle1) != -1:
		return True
	else:
		return False


def is_in_add(cycle, the_cycles):
	number = 0
	for cnt in range(0, len(the_cycles)):
		if is_one(cycle, the_cycles[cnt]):
			number += 1
	if number == 0:
		return the_cycles.append(cycle)
	else:
		return the_cycles


def the_min(s_sequence):
	size = len(s_sequence)
	s_sequence += s_sequence
	fixed_state = s_sequence[0:size]
	
	for j in range(size):
		if s_sequence[j:j + size] < fixed_state:
			fixed_state = s_sequence[j:j + size]
	return fixed_state
	
# list1 = cycles(6)
# for i in range(0, len(list1)):
# 	print('cycle{}'.format(i+1), end='\n')
# 	for k in range(0, len(list1[i])):
# 		print(list1[i][k], end='\n')


def get_s(n):
	cycle_list = []
	# number1 = 0
	# number2 = 0
	seq = ''
	for the_list in cycles(n):
		is_in_add(the_list, cycle_list)
	for i in range(0, len(cycle_list)):
		# k = len(cycle_list[i])
		the_min_list = the_min(cycle_list[i])
		s = ''.join([str(x) for x in the_min_list])
		# if k == 24:
		# 	number1 += 1
		# elif k == 12:
		# 	number2 +=1
		seq += s
		# print(k, s[:k])
	return seq


print(get_s(5))