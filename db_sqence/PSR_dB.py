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


class Run_shift_order:
	def __init__(self,max_run):
		self._shiftlist = []
		self._shiftnumber = 0
		self._run = max_run
	
	def get_number(self, a_list):
		for i in range(0, len(self._shiftlist)):
			if a_list == self._shiftlist[i][0]:
				return self._shiftlist[i][1]
	
	def len(self):
		cnt = 0
		for i in range(0, len(self._shiftlist)):
			if self._shiftlist[i][0][0] == 1:
				cnt += 1
		return cnt
	
	def apend(self, a_list):
		self._shiftlist.append((a_list, self._shiftnumber))
		self._shiftnumber += 1
	
	def if_not_in(self, a_list):
		if len(self._shiftlist) == 0:
			return True
		for i in range(0, len(self._shiftlist)):
			if self._shiftlist[i][0] == a_list:
				return False
		return True
	
	def select_sort(self):
		resort = self._shiftlist
		for i in range(0, len(resort) - 1):
			k = i
			for j in range(i, len(resort)):
				if resort[i][0] < resort[j][0]:
					k = j
			if i != k:
				resort[i], resort[k] = resort[k], resort[i]


def shift_run_number(s_sequence):
	size = len(s_sequence)
	ne_sequence = s_sequence[:]
	ne_sequence += ne_sequence
	
	states = []
	for i in range(size):
		if ne_sequence[i:i + size] not in states:
			states.append(ne_sequence[i:i + size])
	
	states.sort(reverse=True)
	necklace = states[-1]
	max_run = max_run_of0(necklace)
	real_state = necklace[:size - 1]
	real_state += real_state
	real_states = Run_shift_order(max_run)
	
	for i in range(size - 1, -1, -1):
		if real_states.if_not_in(real_state[i:i + size - 1] + [necklace[-1]]) and max_run_of0(real_state[i:i + size - 1] + [necklace[-1]]) == max_run:
			real_states.apend((real_state[i:i + size - 1]) + [necklace[-1]])
	
	real_states.select_sort()
	return real_states.get_number(s_sequence), real_states.len()


def lexi_number(s_sequence):
	size = len(s_sequence)
	s_sequence += s_sequence
	
	states = []
	for i in range(size):
		if s_sequence[i:i + size] not in states:
			states.append(s_sequence[i:i + size])
	
	states.sort(reverse=True)
	return states.index(s_sequence[:size]), len(states)


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


def alg_run_orderA(s_sequence):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		k2, m2 = shift_run_number([1] + state[1:] + [1 - Psr_list(state)])
		k1, m1 = lexi_number(state[1:] + [1 - Psr_list(state)] + [1])
		if (m2 % 2 == 1 and k1 == m1 - 1) or (m2 % 2 == 0 and k2 == 2):
			state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
		else:
			state = state[1:] + [(Psr_list(state) + state[0]) % 2]
		
		retval.append(state[-1])
	
	return retval


if __name__ == '__main__':
	algs = [('A', alg_necklace_order), ('B', alg_run_orderA)]

	for n in range(5, 6):
		start = [0] * n
		for kind, alg in algs:
			s = ''.join([str(x) for x in alg(start)])
			s += s
			idx = s.find('0' * len(start))
			print(n, kind, s[idx:idx + 2 ** (len(start))])
			print(len(s))

