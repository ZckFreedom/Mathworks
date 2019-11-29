def generator_of_all_sequences(sequence_order):
	cnt = 0
	sequence = [0] * sequence_order
	while cnt < 2**sequence_order:
		for bit in range(0, sequence_order):
			a = cnt // (2 ** (sequence_order - 1 - bit))
			sequence[bit] = a % 2
		cnt += 1
		yield sequence


def check_out(ns, s_sequence):
	for state in generator_of_all_sequences(ns):
		se = ''.join([str(x) for x in state])
		if s_sequence.find(se) == -1:
			# print(se)
			# print('it is not a dB_sequence!')
			return 0
	return 1
	# print('Congratulation,this is a dB-sequence for {}!'.format(ns))


# if __name__ == '__main__':
# 	algs = [('A', alg_A), ('B', alg_B), ('C', alg_C), ('D', alg_D), ('E', alg_E)]
#
# 	for n in [5, 9, 17]:
# 		start = [0] * n
# 		for kind, alg in algs:
# 			s = ''.join([str(x) for x in alg(start)])
# 			s += s
# 			# idx = s.find('0' * len(start))
# 			check_out(n, s)
