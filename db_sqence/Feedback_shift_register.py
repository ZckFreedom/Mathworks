from itertools import combinations
import math


def coefficient(list1, list2):      #计算l2中对应于列表l1中为0的位置的成绩，为该项的系数
	the_coefficient = 1
	for i in range(len(list1)):
		if list1[i] == 0:
			the_coefficient *= list2[i]
	return the_coefficient


def single_items(n, k):       #给出n和k，得到所有n长且有k位是1的状态
	all_list = []
	n_group = []
	for i in range(n):
		n_group.append(i)
	all_comb = list(combinations(n_group, k))
	j = 0
	while j < len(all_comb):
		base_list = [0] * n
		for i in range(k):
			base_list[all_comb[j][i]] = 1
		all_list.append(base_list.copy())
		base_list.clear()
		j += 1
	return all_list


def mul_items(list_c):      #给一个n长序列，得到(x1+c1+1)(x2+c2+1)...(xn+cn+1)的所有项
	order = len(list_c)
	c_list = [0] * order
	mul_list = []
	for i in range(order):
		c_list[i] = 1 - list_c[i]
	j = order
	while j > 0:
		all_k = single_items(order, j)
		for i in range(len(all_k)):
			if coefficient(all_k[i], c_list) == 0:
				continue
			mul_list.append(all_k[i])
		j -= 1
	return mul_list


def strs(list1):        #给一个列表，表示成字符的形式
	the_str = ''
	for i in range(len(list1)):
		if list1[i] == 1:
			the_str += 'x{}'.format(i)
	return the_str


def feedback_function(de_sequence):  #给一个debruijn序列，先求出所有需要计算项的序列，然后利用项函数得到各项，相加
	order = int(math.log(len(de_sequence), 2))
	expaision = []
	expaision_str = ''
	for i in range(order, len(de_sequence)):
		if de_sequence[i] == 1:
			mul_item = mul_items(de_sequence[i-order:i])
			for single_item in mul_item:
				if single_item in expaision:
					expaision.remove(single_item)
				else:
					expaision.append(single_item)
	alpha_list = [0] * (order-1)
	sub_list = mul_items(alpha_list)
	for single_item in sub_list:
		sub_item = [0] + single_item
		if sub_item in expaision:
			expaision.remove(sub_item)
		else:
			expaision.append(sub_item)
	if len(expaision) == 0:
		return 0
	for i in range(len(expaision)-1):
		expaision_str += strs(expaision[i])
		expaision_str += '+'
	expaision_str += strs(expaision[-1])
	return expaision_str


def feedback_function_str(de_sequence_str):
	de_sequence = []
	for i in range(len(de_sequence_str)):
		de_sequence.append(int(de_sequence_str[i]))
	return feedback_function(de_sequence)


d = '0000111101100101'
print(feedback_function_str(d))
