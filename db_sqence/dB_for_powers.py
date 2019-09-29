import Polynomials_Field
import time
from randomness_measurements import games_chan


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


def cycles_of_FSR_for6(ns):
	cycle_list = []
	middle_list = []
	mark_number = 0
	for s_sequence in generator_of_all_sequnces(ns):
		for mark in range(0, len(cycle_list)):
			if s_sequence in cycle_list[mark]:
				mark_number = 1
		if mark_number == 0:
			middle_list.append(s_sequence.copy())
			state = s_sequence[1:] + [1 - s_sequence[0]]
			while state != s_sequence:
				middle_list.append(state)
				state = state[1:] + [1 - state[0]]
			cycle_list.append(middle_list.copy())
			middle_list.clear()
		mark_number = 0
	return cycle_list


# list1 = cycles_of_FSR_for6(6)
# for i in range(0, len(list1)):
# 	print(list1[i])


def alg_common_A(s_sequence):
	state = None
	retval = []
	
	size = len(s_sequence)
	cycle_list = cycles_of_FSR(size)
	represent_list = []
	for local in range(0, len(cycle_list)):
		represent_list.append(cycle_list[local][0][:size - 1])
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]

		if state[1:] in represent_list:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def lexi_judge(s_sequence, necklace_list):
	if s_sequence[0] == s_sequence[-1]:
		if (s_sequence[1:] + [1]) in necklace_list:
			return True
		elif (s_sequence[1:] + [0]) in necklace_list:
			return True
		else:
			return False
			
	elif s_sequence[0] != s_sequence[-1]:
		if (s_sequence[1:] + [0]) in necklace_list:
			return True
		elif (s_sequence[1:] + [1]) in necklace_list:
			return True
		else:
			return False


def alg_common_A1(s_sequence):
	state = None
	retval = []
	
	size = len(s_sequence)
	cycle_list = cycles_of_FSR(size)
	represent_list = []
	for local in range(0, len(cycle_list)):
		represent_list.append(cycle_list[local][0])
		
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		if lexi_judge(state, represent_list):
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_common_A2(s_sequence):
	state = None
	retval = []
	
	size = len(s_sequence)
	cycles_list = cycles_of_FSR(size)
	necklace_list = []
	for local in range(0, len(cycles_list)):
		necklace_list.append(cycles_list[local][0])
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		if state[0] == state[-1] and state[1:] + [1 - state[0]] in necklace_list:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		elif state[0] != state[-1] and state[1:] + [state[0]] in necklace_list:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		elif state[0] == 0 and state.count(1) == size - 1:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		elif state.count(1) == size:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_common_B(s_sequence):
	state = None
	retval = []
	
	size = len(s_sequence)
	cycle_list = cycles_of_FSR(size)
	represent_list = []
	for local in range(0, len(cycle_list)):
		cycle_list[local].sort(reverse=True)
		represent_list.append(cycle_list[local][0][:size - 1])
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		if state[1:] in represent_list:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_common_B1(s_sequence):
	state = None
	retval = []
	
	size = len(s_sequence)
	cycle_list = cycles_of_FSR(size)
	represent_list = []
	for local in range(0, len(cycle_list)):
		represent_list.append([1 - x for x in cycle_list[local][0][:size - 1]])
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		if state[1:] in represent_list:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_common_C(s_sequence):
	state = None
	retval = []
	
	size = len(s_sequence)
	cycle_list = cycles_of_FSR(size)
	necklace_list = []
	for local in range(0, len(cycle_list)):
		if cycle_list[local][0][0] == cycle_list[local][0][-1]:
			necklace_list.append(cycle_list[local][0][:size - 1])
		else:
			necklace_list.append([1 - x for x in cycle_list[local][0][:size - 1]])
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		if state[1:] in necklace_list:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def get_representlist(cycle_list):
	size = len(cycle_list[0][0])
	necklace_list = []
	lexi_list = []
	for local in range(0, len(cycle_list)):
		if cycle_list[local][0][0] == cycle_list[local][0][-1]:
			necklace_list.append(cycle_list[local][0][:size - 1])
		else:
			cycle_length = len(cycle_list[local])
			reval = [x[-1] for x in cycle_list[local]]
			reval += reval
			for i in range(0, cycle_length):
				lexi_list.append(reval[i: i + cycle_length])
			lexi_list.sort(reverse=True)
			necklace_list.append(lexi_list[0][: size - 1])
			lexi_list.clear()
	return necklace_list


def alg_common_C1(s_sequence):
	state = None
	retval = []
	
	size = len(s_sequence)
	necklace_list = get_representlist(cycles_of_FSR(size))
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		if state[1:] in necklace_list:
			state = state[1:] + [1 - ((state[0] + state[1] + state[-1]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[1] + state[-1]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_A_for6(s_sequence):
	state = None
	retval = []
	
	size = len(s_sequence)
	cycle_list = cycles_of_FSR_for6(size)
	represent_list = []
	for local in range(0, len(cycle_list)):
		represent_list.append(cycle_list[local][0][:size - 1])
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		if state[1:] in represent_list:
			state = state[1:] + [1 - ((state[0] + state[2] + state[-2]) % 2)]
		else:
			state = state[1:] + [(state[0] + state[2] + state[-2]) % 2]
		
		retval.append(state[-1])
	
	return retval


if __name__ == '__main__':
	algs = [('A', alg_common_A), ('A1', alg_common_A1), ('A2', alg_common_A2), ('B', alg_common_B),
	        ('B1', alg_common_B1), ('C', alg_common_C), ('C1', alg_common_C1)]

	for n in range(5, 16):
		start_time = time.perf_counter()
		start = [0] * n
		for kind, alg in algs:
			if kind == 'C':
				s = ''.join([str(x) for x in alg(start)])
				s += s
				idx = s.find('0' * len(start))
				if len(kind) == 1:
					space_number = 1
				else:
					space_number = 0
				print(n, kind, ' '*space_number, s[idx:idx + 2 ** (len(start))])
				print(2 ** n)
				print(games_chan(s))
				# print(time.perf_counter() - start_time, "seconds")
