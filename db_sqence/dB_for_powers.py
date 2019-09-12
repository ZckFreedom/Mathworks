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
def cycles_of_FSR():
	cycle_list = []
	cycle_list1 = []
	middle_list = []
	all_sequences = []
	for sequences in generator_of_all_sequnces(5):
		all_sequences.append(sequences.copy())
	for i in range(0, len(all_sequences)):
		s = all_sequences[i]
		middle_list.append(s)
		state = s[1:] + [(s[0] + s[1] + s[4]) % 2]
		while state != s:
			middle_list.append(state)
			state = state[1:] + [(state[0] + state[1] + state[4]) % 2]
		middle_list.sort()
		cycle_list.append(middle_list.copy())
		middle_list.clear()
	for x in cycle_list:
		if x not in cycle_list1:
			cycle_list1.append(x)
	return cycle_list1


list1 = cycles_of_FSR()
for i in range(0, len(list1)):
	print(list1[i])
