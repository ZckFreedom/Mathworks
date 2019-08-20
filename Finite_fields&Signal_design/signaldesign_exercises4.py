from fundamental_tools.Polynomials_Field import PolynomialsField,FieldError
import sys
sys.setrecursionlimit(10000)


def f(list1):
	a = list1[0]
	b = list1[1]
	c = list1[2]
	d = list1[3]
	e = list1[4]
	f = list1[5]
	g = list1[6]
	# h = list1[7]
	# i = list1[8]
	# j = list1[9]
	x = (a + b)%2
	list1 = [b,c,d,e,f,g,x]
	return list1


# a = [1,0,0,0,0,0,0]
# i = 0
# while i<50:
# 	print(a,end='\n')
# 	a = f(a)
# 	i +=1

def is_a_q_for_2(q):    #判断是否是2的幂次
	if not isinstance(q, int):
		raise ValueError('我需要整数')
	if q ==1:
		return True
	elif q%2 == 0:
		return is_a_q_for_2(int(q/2))
	else:
		return False


def is_a_primitive_of_2(q): #判断是否是2的幂次减1，即是否可能是本原元的次数
	q +=1
	if is_a_q_for_2(q):return True
	else:return False


def product_n_unity_polynimial(n,p):    #生成一个阶为n的单位多项式
	list1 = [1]
	list2 = [0]*(n-1)
	list1.extend(list2)
	list1.append(1)
	return PolynomialsField(list1,p)


def factor(n):  #取得一个数的所有因子
	list1 =[]
	for i in range(2,n//2+1):
		if n%i ==0:list1.append(i)
	return list1


def is_a_primitivepolymonial_of_n(f):   #判断一个多项式是否是本原多项式
	if not isinstance(f,PolynomialsField):
		raise FieldError('这不是多项式')
	n = f._deg
	p = f._mod
	the_number = 2**n -1
	the_list = factor(the_number)
	if len(the_list) == 0:
		return True
	for i in the_list:
		if i>n:
			g = product_n_unity_polynimial(i,p)
			if g % f == 0:
				return False
	return True


def verify_the_function(n):
	list1 = [1]
	list2 = [0] * (n - 1)
	list1.extend(list2)
	list1.append(1)
	for i in range(2, n - 2):
		for j in range(i + 1, n - 1):
			for k in range(j + 1, n):
				list1[i], list1[j], list1[k] = 1, 1, 1
				f = PolynomialsField(list1, 2)
				if is_a_primitivepolymonial_of_n(f):
					print(f, 'is the primitive for degree{} '.format(n))
					return True
	list1.clear()
	list2.clear()
	# print('没有{}阶的本原5项式'.format(n))
	return False


def verify_the_result():
	n = 5
	while n<16:
		if verify_the_function(n):pass
		else:
			print('没有{}阶的本原5项式'.format(n))
		n +=1
	


verify_the_result()

