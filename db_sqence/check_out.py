from dB_for_powers import generator_of_all_sequnces,alg_A



def check_out(n, s_sequsence):
	for state in generator_of_all_sequnces(n):
		s = ''.join([str(x) for x in state])
		if s_sequsence.find(s) == -1:
			print(s)
			print('it is not a dB_sequence!')
			return


if __name__ == '__main__':
	algs = [('A', alg_A)]
	
	for n in [5, 9]:
		start = [0] * n
		for kind, alg in algs:
			s = ''.join([str(x) for x in alg(start)])
			s += s
			# idx = s.find('0' * len(start))
			check_out(n, s)
