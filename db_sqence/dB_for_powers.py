import Polynomials_Field


def generator_of_all_sequnces(sequence_order):
	cnt = 0
	sequence = [0] * sequence_order
	while cnt < 2**sequence_order:
		for bit in range(0, sequence_order):
			a = cnt // (2 ** (sequence_order - 1 - bit))
			sequence[bit] = a % 2
		cnt += 1
		yield sequence


def list_of_powers(powers_order):
	func_f = (Polynomials_Field.PolynomialsField([1, 1], 2)) ** powers_order
	return func_f.get_body()


# list1 = list_of_powers(5)
# for i in range(0, len(list1)):
# 	print(list1[i].get_body(), end=' ')
def cycles_of_FSR(ns):
	cycle_list = []
	middle_list = []
	mark_number = 0
	for s_sequence in generator_of_all_sequnces(ns):
		for mark in range(0, len(cycle_list)):
			if s_sequence in cycle_list[mark]:
				mark_number = 1
		if mark_number == 0:
			middle_list.append(s_sequence.copy())
			state = s_sequence[1:] + [(s_sequence[0] + s_sequence[1] + s_sequence[-1]) % 2]
			while state != s_sequence:
				middle_list.append(state)
				state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
			cycle_list.append(middle_list.copy())
			middle_list.clear()
		mark_number = 0
	return cycle_list


# list1 = cycles_of_FSR(5)
# for i in range(0, len(list1)):
# 	print(list1[i])


def if_final_lexi_min(s_sequence):
	represent_sequence = s_sequence[1:]
	size = len(s_sequence)
	cycle_list = cycles_of_FSR(size)
	represent_list = []
	for state in range(0, len(cycle_list)):
		represent_list.append(cycle_list[state][0][:size-1])
	
	if represent_sequence in represent_list:
		return True
	else:
		return False


def alg_A(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]

		if if_final_lexi_min(state):
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


if __name__ == '__main__':
	algs = [('A', alg_A)]

	for n in [5, 9]:
		start = [0] * n
		for kind, alg in algs:
			s = ''.join([str(x) for x in alg(start)])
			s += s
			idx = s.find('0' * len(start))
			print(n, kind, s[idx:idx + 2 ** (len(start))])
			print(len(s))
