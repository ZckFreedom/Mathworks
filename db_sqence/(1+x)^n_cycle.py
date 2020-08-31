from important_character import games_chan


def generator_of_all_sequnces(sequence_order):
	cnt = 0
	sequence = [0] * sequence_order
	while cnt < 2**sequence_order:
		for bit in range(0, sequence_order):
			a = cnt // (2 ** (sequence_order - 1 - bit))
			sequence[bit] = a % 2
		cnt += 1
		yield sequence


def find_order(n_number):
	pow_number = 1
	order = 0
	while pow_number < n_number:
		pow_number *= 2
		order += 1
	return order


def if_in(a_sequence, all_cycles):       #输入一个序列和一个cycle集合，判断该序列是否在这些cycle中出现过
	for j in range(len(all_cycles)):
		if a_sequence in all_cycles[j]:
			return True
	return False


def binary_set(k_number):       #输入一个整数，输出这个整数二进制表示是1的那些位置的列表
	k_binary = bin(k_number).replace('0b', '')
	binary_list = []
	binary_len = len(k_binary) - 1
	for j in range(binary_len + 1):
		if k_binary[j] == '1':
			binary_list.append(binary_len - j)
	return binary_list


def set_including(set1, set2):      #输入n和i的二进制为1的位置列表，输出Si是否包含于Sn的判断
	if len(set2) == 0:
		return True
	for j in range(len(set2)):
		if set2[j] not in set1:
			return False
	return True


def coeffcient_list(n_number):      #输入n，输出（1+x）^n的低于n次的所有项的系数
	coe_list = [0] * n_number
	n_set = binary_set(n_number)
	for j in range(n_number):
		if set_including(n_set, binary_set(j)):
			coe_list[j] = 1
	return coe_list


def cycle_lists(n_number):      #输入n，输出特征多项式为（1+x）^n的cycle
	cycle_list = []
	middle_list = []
	coe_list = coeffcient_list(n_number)
	for sequence in generator_of_all_sequnces(n_number):
		if if_in(sequence, cycle_list):
			continue
		middle_list.append(sequence.copy())
		next_bit = 0
		for j in range(len(coe_list)):
			if coe_list[j] == 1:
				next_bit += sequence[j]
		state = sequence[1:] + [next_bit % 2]
		while state != sequence:
			middle_list.append(state.copy())
			next_bit = 0
			for j in range(len(coe_list)):
				if coe_list[j] == 1:
					next_bit += state[j]
			state = state[1:] + [next_bit % 2]
		cycle_list.append(middle_list.copy())
		middle_list.clear()
	return cycle_list


def str_cycle(a_cycle):     #输入一个cycle的所有状态，输出这个cycle的字符串形式，输出的长度为2的k次方形式，k为2的k次方大于n的最小数
	order = len(a_cycle)
	if order < len(a_cycle[0]):
		the_k = pow(2, find_order(len(a_cycle[0])))
		cycle_list = a_cycle[0][:order]
		cycle_list *= int(the_k/order)
	else:
		cycle_list = a_cycle[0]
	next_state = 1
	while len(cycle_list) < order:
		cycle_list.append(a_cycle[next_state][-1])
		next_state += 1
	cycle_str = ''.join([str(x) for x in cycle_list])
	return cycle_str


def hamming_weight(a_sequence):     #输入一个cycle字符串，输出其汉明重量
	weight = 0
	for j in range(len(a_sequence)):
		if a_sequence[j] == '1':
			weight += 1
	return weight


def cycles_character(n_number):      #输入n，输出特征多项式为（1+x）^n的cycle的一些性质
	all_cycles = cycle_lists(n_number)
	cycle_number = len(all_cycles)
	print('order:', n_number)
	print('cycles number:', cycle_number)
	print('-------------------------')
	for j in range(cycle_number):
		the_cycle = str_cycle(all_cycles[j])
		linear_span = games_chan(the_cycle)
		ha_weight = hamming_weight(the_cycle)
		print('cycle:', the_cycle)
		print('linear span:', linear_span)
		print('hamming weight', ha_weight)
		print('-------------------------')

# def cycles_number(n_number):
# 	the_k = find_order(n_number)
# 	cycle_number1 = 2
# 	cycle_number2 = 2
# 	for j in range(1, the_k):
# 		cycle_number1 += pow(2, pow(2, j-1)-j) * (pow(2, pow(2, j-1)) - 1)
# 	for j in range(3, the_k):
# 		cycle_number2 += pow(2, pow(2, j-1)-j)
# 	cycle_number2 += pow(2, pow(2, the_k-1) - the_k + 1)
# 	remain_term = pow(2, pow(2, the_k-1) - the_k) * (pow(2, n_number - pow(2, the_k-1)) - 1)
# 	cycle_number1 += remain_term
# 	cycle_number2 += remain_term
# 	return cycle_number1, cycle_number2
#
#
# for i in range(4, 15):
# 	cycles_character(i)
# 	print(cycles_number(i))


cycles_character(9)
