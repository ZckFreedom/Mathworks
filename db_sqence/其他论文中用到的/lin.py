def weight(s_sequence):
	"""
	给一个状态，求重量
	"""
	weight_number = 0
	for i in range(0, len(s_sequence)):
		if s_sequence[i] == 1:
			weight_number += 1
	return weight_number


def find_conk(s_sequence):
	"""
	给一个状态，找到这个状态所在圈的conecklace
	"""
	size = len(s_sequence)
	states = s_sequence
	
	s = s_sequence[:]
	for i in range(size):
		s.append(1 - s_sequence[i])
	s += s
	for i in range(2 * size):
		if s[i:i + size] < states:
			states = s[i:i + size]
	return states


def find_kth(s_sequence, k_number, case):   # s_sequence是目前状态，k_number是给的k值，case是对应定理
	n = len(s_sequence)  # 状态长度
	co_nk = find_conk(s_sequence)   # 找到conecklace
	cycles = co_nk.copy()
	for i in range(n):
		cycles.append(1 - co_nk[i])
	cycles += cycles        # 得到两个循环的圈
	co_weight = weight(co_nk)   # conecklace的重量
	if co_weight == 0:      # 如果conecklace的重量小于1，则直接返回错误
		return False
	the_one_number = 0      # 用来计数，看移位到了第几个1
	if case == 1:
		for i in range(2*n, 3*n):
			if cycles[i] == 1:
				the_one_number += 1     # 遇到一个1计数变量就加一个1
				if the_one_number == 1 and co_weight < k_number:    # 如果是第一个1而且重量小于k
					return cycles[i+1-n:i+1] == s_sequence      # 判断对应移位规则后的状态是否相等，相等则返回正确
				elif the_one_number == k_number and co_weight >= k_number:   # 如果是第k个1
					return cycles[i+1-n:i+1] == s_sequence      # 判断对应移位规则后的状态是否相等，相等则返回正确
	elif case == 2:
		for i in range(3*n-1, 2*n, -1):
			if cycles[i] == 1:
				the_one_number += 1
				if the_one_number == 1 and co_weight < k_number:
					return cycles[i:i+n] == s_sequence
				elif the_one_number == k_number and co_weight >= k_number:
					return cycles[i:i+n] == s_sequence
	elif case == 3:
		for i in range(2*n, 3*n):
			if cycles[i] == 1:
				the_one_number += 1
			if the_one_number == 1 and (k_number % 2) == 1:
				return cycles[i+1-n:i+1] == s_sequence
			elif the_one_number == co_weight and (k_number % 2) == 0:
				return cycles[i+1-n:i+1] == s_sequence


def find_kth_for4(s_sequence, k_number, t_number):   # s_sequence是目前状态，k_number是给的k值，case是对应定理
	n = len(s_sequence)  # 状态长度
	co_nk = find_conk(s_sequence)   # 找到conecklace
	cycles = co_nk.copy()
	for i in range(n):
		cycles.append(1 - co_nk[i])
	cycles += cycles        # 得到两个循环的圈
	co_weight = weight(co_nk)   # conecklace的重量
	if co_weight == 0:      # 如果conecklace的重量小于1，则直接返回错误
		return False
	the_one_number = 0      # 用来计数，看移位到了第几个1
	for i in range(2*n, 3*n):
		if cycles[i] == 1:
			the_one_number += 1     # 遇到一个1计数变量就加一个1
			if the_one_number == 1 and co_weight < t_number:    # 如果是第一个1而且重量小于t
				return cycles[i+1-n:i+1] == s_sequence      # 判断对应移位规则后的状态是否相等，相等则返回正确
			elif the_one_number == t_number and t_number <= co_weight < k_number:
				return cycles[i+1-n:i+1] == s_sequence
			elif the_one_number == k_number and co_weight >= k_number:   # 如果是第k个1
				return cycles[i+1-n:i+1] == s_sequence      # 判断对应移位规则后的状态是否相等，相等则返回正确

	
def algorithm_A(s_sequence, k_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		next_state = state[1:] + [1]        # 定理中的α
		answer = find_kth(next_state, k_number, 1)     # answer作为一个判断，判断next_state是否等于定理A1中的移位状态
		if answer:
			state = state[1:] + [state[0]]
		else:
			state = state[1:] + [1 - state[0]]
		
		retval.append(state[-1])
	
	return retval


def algorithm_B(s_sequence, k_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		next_state = [1] + state[1:]
		answer = find_kth(next_state, k_number, 2)
		if answer:
			state = state[1:] + [state[0]]
		else:
			state = state[1:] + [1 - state[0]]
		
		retval.append(state[-1])
	
	return retval


def algorithm_C(s_sequence, k_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
			
		next_state = state[1:] + [1]
		answer = find_kth(next_state, k_number, 3)
		if answer:
			state = state[1:] + [state[0]]
		else:
			state = state[1:] + [1 - state[0]]
		
		retval.append(state[-1])
	
	return retval


def algorithm_D(s_sequence, k_number, t_number):
	state = None
	retval = []
	
	while state != s_sequence:
		if state is None:
			state = s_sequence[:]
		
		next_state = state[1:] + [1]
		answer = find_kth_for4(next_state, k_number, t_number)
		if answer:
			state = state[1:] + [state[0]]
		else:
			state = state[1:] + [1 - state[0]]
		
		retval.append(state[-1])
	
	return retval


algs = [('A1', algorithm_A), ('A2', algorithm_B), ('A3', algorithm_C), ('A4', algorithm_D)]
"""
algs是包含四个算法和对应定理的列表
下面的代码作用是给定n的范围，然后生成一个n长0状态，从这个状态开始， 可以改变start使得从任何一个状态开始
然后对于前三个定理，取遍k的所有可能对应的db序列
对于最后一个定理，取遍k，t的所有可能对应的db序列
"""
for n in range(6, 7):
	start = [0] * n
	for kind, alg in algs[:3]:
		for k in range(1, n):
			s = ''.join([str(x) for x in alg(start, k)])    # 把对应算法得到的db序列改写成列表的形式
			s += s      # 得到两个周期的序列，为了取其中的2**n长度
			idx = s.find('0' * len(start))  # 找到n长的0所在的位置，从n长的0开始输出序列
			print(n, k, kind, s[idx:idx + 2 ** (len(start))])   # 输出n，k，对应的定理和对应的db序列
			# print(len(s)//2)
	for k in range(2, n):
		for t in range(1, k):
			s = ''.join([str(x) for x in algs[3][1](start, k, t)])
			s += s
			idx = s.find('0' * len(start))
			print(n, k, t, algs[3][0], s[idx:idx + 2 ** (len(start))])
			# print(len(s) // 2)
