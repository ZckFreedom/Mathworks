from fundamental_tools.A_way_of_q_Field import *


def r3_for_2(list1, t):
	n = len(list1)
	c = 0
	for j in range(0,n):
		c += (-1)**(list1[j] + list1[(j+t) % n])
	return c


def kai(x_list, f_list, p):
	f = PolynomialsField(f_list, p)
	x = Field_q(x_list, f)
	a = x.trace().get_body().get_body()[0].get_body()
	return a
