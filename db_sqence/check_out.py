from dB_for_powers import *


def check_out(ns, s_sequsence):
	for state in generator_of_all_sequnces(ns):
		se = ''.join([str(x) for x in state])
		if s_sequsence.find(se) == -1:
			print(se)
			print('it is not a dB_sequence!')
			return
	print('Congratulation,this is a dB-sequence for {}!'.format(ns))


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
