import time
from scipy.special import comb

start_time = time.perf_counter()


class field_list:
	def __init__(self, element_list):
		self._list = element_list
	
	def __add__(self, other):
		add_list = []
		for i in range(0, len(self._list)):
			add_list.append((self._list[i] + other.get_list()[i]) % 3)
		return field_list(add_list)
	
	def get_list(self):
		return self._list


def delete_zero(divisor_list):
	while True:
		if divisor_list[0] == 0:
			divisor_list.pop(0)
		else:
			break


def list_mod(primitive_ply, element_ply):       # 得到给的元素的基表示形式
	n = len(primitive_ply)-1
	m = len(element_ply)
	if m < n:
		norm_list = [0] * (n-m)
		norm_list += element_ply
		return norm_list
	else:
		while m > n:
			diply = primitive_ply + [0] * (m-n)
			for i in range(m):
				element_ply[i] = (element_ply[i] - diply[i]) % 3
			delete_zero(element_ply)
			m = len(element_ply)
		if m < n:
			return [0]*(n-m) + element_ply
		else:
			return element_ply


def T1_T2_list(primitive_list):
	n = len(primitive_list) - 1
	# T1_list = []
	T2_list = []
	for i in range(0, 3**n-1):
		element_list = [1] + [0] * i
		element_norm = list_mod(primitive_list, element_list)
		# if element_norm[1] == 1:
		# 	T1_list.append(element_norm)
		# c1, c2 = element_norm[0], element_norm[1]
		c1 = element_norm[0]
		# if (c1 == 2 and c2 != 2) or (c1 != 2 and c2 == 2):
		# 	T2_list.append(element_norm)
		# elif c1 == 2 and c2 == 2:
		# 	T2_list.append(element_norm)
		# 	T2_list.append(element_norm)
		if c1 == 2:
			T2_list.append(element_norm)
	return T2_list


def the_sum(ply_list):
	n = len(ply_list) - 1
	u_sum = [0] * n
	u_index = 0
	# u_index_list = [0] * n
	e_number = 3**(n-1) - n + 1
	# T1, T2 = T1_T2_list(ply_list)
	T2 = T1_T2_list(ply_list)
	# for j in range(n):
	# 	# number = ((n-4)//5) // (3 ** (n - 1 - j))
	# 	# e_list[j] = number
	
	while u_index < e_number + 1:
		# for j in range(n):
		# 	number = u_index // (3 ** (n - 1 - j))
		# 	u_index_list[j] = number
		#
		# count_add = 0
		# for i in range(0, n):
		# 	if e_list[i] == 2 and u_index_list[i] > 0:
		# 		count_add += 1
		# 	if e_list[i] == 1 and u_index_list[i] == 2:
		# 		count_add += 1
		# if count_add == 0:
		# 	if u_index <= 3**(n-1) - 1:
		# 		u_sum += field_list(T1[u_index])
		# 	else:
		# 		u_sum += field_list(T2[u_index - 3**(n-1)])
		if comb(e_number, u_index) % 3 != 0:
			for i in range(n):
				u_sum[i] += int(comb(e_number, u_index)) * (-1)**(e_number-u_index) * T2[u_index][i]

		u_index += 1
	for i in range(n):
		u_sum[i] = u_sum[i] % 3
	return u_sum


h1 = [1, 1, 0, 0, 2]
print(the_sum(h1))
print(time.perf_counter() - start_time, "seconds")
