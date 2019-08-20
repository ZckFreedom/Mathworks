class FieldError(ValueError):
	pass


'''
只先定义素域的定义，定义简单的加减乘除和求逆，每个对象是素域中的一个元素
如果有需要，可以定义另一个类，其每个对象是一个域，元素个数为p
用来探究域中的本原元，阶相同的元素个数，不同的轨道等性质
'''


class Field_p:
	def __init__(self, n, p):
		if isinstance(n, int):
			self._home = p
			self._body = n % self._home
		elif isinstance(n, Field_p):
			self._home = n._home
			self._body = n._body
	
	def __add__(self, other):
		if self._home != other.get_home():
			raise FieldError('不在同一个域里面，不能加')
		p = self._home
		return Field_p(self._body + other.get_body(), p)
	
	def __sub__(self, other):
		if self._home != other.get_home():
			raise FieldError('不在同一个域里面，不能减')
		p = self._home
		return Field_p(self._body - other.get_body(), p)
	
	def __mul__(self, other):
		if self._home != other.get_home():
			raise FieldError('不在同一个域里面，不能乘')
		p = self._home
		return Field_p(self._body * other.get_body(), p)
	
	def inverse(self):
		p = self._home
		a = self._body
		i = 0
		while True:
			'''#因为p是素数时候一定有逆'''
			if (1 + i*p) % a == 0:
				return Field_p(int((1 + i*p)/a), p)
			i += 1
	
	def __truediv__(self, other):
		if self._home != other.get_home():
			raise FieldError('不在同一个域里面，不能除')
		p = self._home
		return Field_p(other.inverse() * self, p)
	
	def __eq__(self, other):
		return self._body == other.get_body()
	
	def ord(self):
		p = self._home
		a = self._body
		b = 1
		for i in range(1, p):
			b = (b*a) % p
			if b == 1:
				return i

	def __str__(self):
		return str(self._body)
	
	def get_body(self):
		return self._body
	
	def get_home(self):
		return self._home
	

# list1 = [0] *0
# list2 = list1[1:].copy()
# list3 = [5]
# list3.extend(list1)
# list1.append(0)
# for i in range(0, len(list1)):
# 	list1[i] = 2 * list1[i]
# print(list1)
# a = Field_p(4,5)
# b = Field_p(2,5)
# print(a/b)
