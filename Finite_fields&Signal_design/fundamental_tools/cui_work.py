import time
from A_way_of_q_Field import *


start_time = time.perf_counter()


def T1_reflection(element, order):
	if len(element.get_body().get_body()) < order - 1:
		return 0
	elif len(element.get_body().get_body()) == order - 1:
		return element.get_body().get_body()[0].get_body()
	elif len(element.get_body().get_body()) == order:
		return element.get_body().get_body()[1].get_body()


def T2_reflection(element, order):
	if len(element.get_body().get_body()) < order - 1:
		return 0, 0
	elif len(element.get_body().get_body()) == order - 1:
		return 0, element.get_body().get_body()[0].get_body()
	elif len(element.get_body().get_body()) == order:
		return element.get_body().get_body()[0].get_body(), element.get_body().get_body()[1].get_body()


def T1_T2_list(a_irreducible_ply, order):
	T1_list = []
	T2_list = []
	for i in range(0, 3**order - 1):
		element_list = [1] + [0] * i
		the_element = Field_q(element_list, a_irreducible_ply)
		if T1_reflection(the_element, order) == 1:
			T1_list.append(the_element)
		c1, c2 = T2_reflection(the_element, order)
		if (c1 == 2 and c2 != 2) or (c1 != 2 and c2 == 2):
			T2_list.append(the_element)
		elif c1 == 2 and c2 == 2:
			T2_list.append(the_element)
			T2_list.append(the_element)
	return T1_list, T2_list


def the_sum(ply_list):
	ply = PolynomialsField(ply_list, 3)
	n = len(ply_list) - 1
	u_index = 0
	e_list = [0] * n
	u_index_list = [0] * n
	u_sum = Field_q([0], ply)
	u_sum1 = Field_q([0], ply)
	T1, T2 = T1_T2_list(ply, n)
	
	for j in range(n):
		a = ((n-3)//4) // (3 ** (n - 1 - j))
		e_list[j] = a
		
	while u_index < 3 ** n:
		for j in range(n):
			a = u_index // (3 ** (n - 1 - j))
			u_index_list[j] = a
		
		count_add = 0
		for i in range(0, n):
			if e_list[i] == 2 and u_index_list[i] > 0:
				count_add += 1
			if e_list[i] == 1 and u_index_list[i] == 2:
				count_add += 1
		if u_index <= 3 ** (n - 1) - 1:
			u_sum1 += T1[u_index]
		else:
			u_sum1 += T2[u_index - 3 ** (n - 1)]
		if count_add == 0:
			if u_index <= 3**(n-1) - 1:
				u_sum += T1[u_index]
			else:
				u_sum += T2[u_index - 3**(n-1)]
		
		u_index += 1
	
	print(u_index)
	return u_sum


h1 = [1, 1, 0, 1, 0, 0, 0, 1]
print(the_sum(h1))
print(time.perf_counter() - start_time, "seconds")