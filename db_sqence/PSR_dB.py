from check_out import check_out


def Psr_list(s_sequence):
	size = len(s_sequence)
	sums = 0
	
	for i in range(1, size):
		sums = (sums + s_sequence[i]) % 2
	return sums


def max_run_of0(s_sequence):
	cnt = 0
	counter = []
	
	for i in range(0, len(s_sequence)):
		if s_sequence[i] == 1:
			counter.append(cnt)
			cnt = 0
		elif s_sequence[i] == 0:
			cnt += 1
	counter.append(cnt)
	
	counter.sort()
	return counter[-1]


def find_nk(s_sequence):
	size = len(s_sequence)
	state = s_sequence[:]
	state += state
	states = []
	
	for i in range(0, size):
		if state[i: i + size] not in states:
			states.append(state[i: i + size])
	
	states.sort()
	return states[0]


def shift_order_psr(s_sequence):
	size = len(s_sequence)
	cycle = [(Psr_list(s_sequence) + s_sequence[0]) % 2] + s_sequence
	nk = find_nk(cycle)
	l_number = find_l(nk)
	cycle += cycle
	
	left_shift = Shift_order_space()
	
	for i in range(0, size+1):
		if left_shift.check(cycle[i:i + size + 1]):
			left_shift.append(cycle[i:i + size + 1])
	
	return left_shift.get_number(nk) % (size+1), l_number, left_shift.get_len()


class Shift_order_space:
	def __init__(self):
		self._shiftlist = []
		self._shiftnumber = 0
	
	def get_number(self, a_list):
		for i in range(0, len(self._shiftlist)):
			if a_list == self._shiftlist[i][0]:
				return self._shiftlist[i][1]
		return -1
	
	def get_len(self):
		return self._shiftnumber
	
	def append(self, a_list):
		self._shiftlist.append((a_list, self._shiftnumber))
		self._shiftnumber += 1
	
	def if_not_in(self, a_list):
		if len(self._shiftlist) == 0:
			return True
		for i in range(0, len(self._shiftlist)):
			if self._shiftlist[i][0] == a_list:
				return False
		return True
	
	def check(self, a_list):
		if self.if_not_in(a_list) is not True:
			return False
		return a_list[-1] == 1


class Run_shift_order:
	def __init__(self, max_run):
		self._shiftlist = []
		self._shiftnumber = 0
		self._run = max_run
	
	def get_number(self, a_list):
		for i in range(0, len(self._shiftlist)):
			if a_list == self._shiftlist[i][0]:
				return self._shiftlist[i][1]
		return -1
	
	def get_len(self):
		return self._shiftnumber
	
	def append(self, a_list):
		self._shiftlist.append((a_list, self._shiftnumber))
		self._shiftnumber += 1
	
	def if_not_in(self, a_list):
		if len(self._shiftlist) == 0:
			return True
		for i in range(0, len(self._shiftlist)):
			if self._shiftlist[i][0] == a_list:
				return False
		return True
	
	def check(self, a_list):
		if self.if_not_in(a_list) is not True:
			return False
		cnt = 0
		for i in a_list[1:]:
			if i == 0:
				cnt += 1
			else:
				break
		return cnt == self._run


def shift_run_number(s_sequence):
	size = len(s_sequence)
	nk = find_nk(s_sequence)
	max_run = max_run_of0(nk)
	nk += nk
	max_run_states = Run_shift_order(max_run)
	
	for i in range(size - 1, 0, -1):
		if max_run_states.check(nk[i:i + size]):
			max_run_states.append(nk[i:i + size])
	
	return max_run_states.get_number(s_sequence), max_run_states.get_len()


def lexi_number(s_sequence):
	size = len(s_sequence)
	s_sequence += s_sequence
	
	states = []
	for i in range(size):
		if s_sequence[i:i + size] not in states:
			states.append(s_sequence[i:i + size])
	
	states.sort(reverse=True)
	return states.index(s_sequence[:size]), len(states)


def all_divisor(number):
	divisor = [number]
	for i in range(1, number // 2):
		if number % i == 0:
			divisor.append(i)
	return divisor


def find_l(sequence):
	length = len(sequence)
	length_divisor = all_divisor(length)
	number_l = 0
	for d in length_divisor:
		if sequence[:d] == sequence[length - d:length]:
			for i in range(0, d):
				if sequence[i] == 1:
					number_l += 1
			return number_l


def alg_necklace_order(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		k, m = lexi_number(state[1:] + [1 - Psr_list(state)] + [1])
		if k == m - 1:
			state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
		else:
			state = state[1:] + [(Psr_list(state) + state[0]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_run_orderA(s_sequence, k_number):  # F1
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		local, m = shift_run_number([1] + state[1:] + [1 - Psr_list(state)])
		next_state = state[1:] + [1 - Psr_list(state)] + [1]
		if m >= k_number and local == k_number - 1 or m < k_number and next_state == find_nk(next_state):
			state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
		else:
			state = state[1:] + [(Psr_list(state) + state[0]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_run_orderB(s_sequence):  # F2
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		local, m = shift_run_number([1] + state[1:] + [1 - Psr_list(state)])
		next_state = state[1:] + [1 - Psr_list(state)] + [1]
		if m % 2 == 0 and local == 1 or m % 2 == 1 and next_state == find_nk(next_state):
			state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
		else:
			state = state[1:] + [(Psr_list(state) + state[0]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_shift_orderA(s_sequence, k_number):  # G1
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		local, m, k = shift_order_psr([1] + state[1:])
		next_state = state[1:] + [1 - Psr_list(state)] + [1]
		if m >= k_number and local == k_number or m < k_number and next_state == find_nk(next_state):
			state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
		else:
			state = state[1:] + [(Psr_list(state) + state[0]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_shift_orderB(s_sequence, k_number, t_number):  # G2
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		local, m, k = shift_order_psr([1] + state[1:])
		next_state = state[1:] + [1 - Psr_list(state)] + [1]
		if m >= k_number and local == k_number:
			state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
		elif (t_number <= m < k_number) and local == t_number:
			state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
		elif m < t_number and next_state == find_nk(next_state):
			state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
		else:
			state = state[1:] + [(Psr_list(state) + state[0]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_shift_orderC(s_sequence):  # G3
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		local, m, k = shift_order_psr([1] + state[1:])
		next_state = state[1:] + [1 - Psr_list(state)] + [1]
		if m % 2 == 1 and local == 1 or m % 2 == 0 and next_state == find_nk(next_state):
			state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
		else:
			state = state[1:] + [(Psr_list(state) + state[0]) % 2]
		
		retval.append(state[-1])
	
	return retval


def alg_shift_order(s_sequence, k):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		local, ly1, states = shift_order_psr(state[1:] + [1])
		if k % ly1 == 0 and local == (k-1) % states or k % ly1 != 0 and local == k % states:
			state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
		else:
			state = state[1:] + [(Psr_list(state) + state[0]) % 2]
		
		retval.append(state[-1])
	
	return retval

# if __name__ == '__main__':
# 	algs = [('F1', alg_run_orderA), ('F2', alg_run_orderB),
# 	        ('G1', alg_shift_orderA), ('G2', alg_shift_orderB), ('G3', alg_shift_orderC)]
#
# 	for n in range(6, 7):
# 		start = [0] * n
# 		for kind, alg in algs:
# 			if kind == 'G2':
# 				for k in range(2, n):
# 					for t in range(1, k):
# 						s = ''.join([str(x) for x in alg(start, k, t)])
# 						s += s
# 						idx = s.find('0' * len(start))
# 						print(n, k, t, kind, s[idx:idx + 2 ** (len(start))])
# 			elif kind == 'F1' or kind == 'G1':
# 				for k in range(1, n):
# 					s = ''.join([str(x) for x in alg(start, k)])
# 					s += s
# 					idx = s.find('0' * len(start))
# 					print(n, k, kind, s[idx:idx + 2 ** (len(start))])
# 			else:
# 				s = ''.join([str(x) for x in alg(start)])
# 				s += s
# 				idx = s.find('0' * len(start))
# 				print(n, kind, s[idx:idx + 2 ** (len(start))])


start = [0] * 6
db_sequences = []
for ks in range(1, 20):
	s = ''.join([str(x) for x in alg_shift_order(start, ks)])
	s += s
	idx = s.find('0' * len(start))
	if s[idx:idx + 2 ** (len(start))] not in db_sequences:
		db_sequences.append(s[idx:idx + 2 ** (len(start))])
		print('k={}'.format(ks), s[idx:idx + 2 ** (len(start))])
# print(len(db_sequences))
