from fundamental_tools.A_way_of_q_Field import *


class PolynomialsForFq:
	@staticmethod
	def initialize(list1, p):
		if isinstance(list1, int):
			return [list1]
		if len(list1) == 0:
			return [0]
		if isinstance(list1[0], int):
			for i in range(0, len(list1)):
				if list1[i] != 0:
					return list1[i:]
		elif isinstance(list1[0], Field_q):
			for i in range(0, len(list1)):
				if list1[i].get_body() != PolynomialsField(0, p):
					return list1[i:]
		return [0]
	
	def __init__(self, list1, a_irreducible_polynomial):
		list2 = PolynomialsForFq.initialize(list1, a_irreducible_polynomial.get_home())
		self._body = []
		for i in range(0, len(list2)):
			if isinstance(list2[i], Field_q):
				self._body.append(list2[i])
			else:
				self._body.append(Field_q(list2[i], a_irreducible_polynomial))
		if len(list2) == 1:
			if isinstance(list2[0], int) and list2[0] == 0:
				self._deg = -1
			elif isinstance(list2[0], Field_q) and list2[0] == Field_q(0, a_irreducible_polynomial):
				self._deg = -1
			else:
				self._deg = 0
		else:
			self._deg = len(list2) - 1
		self._mother = a_irreducible_polynomial
		
	def __add__(self, other):
		zero = Field_q(0, self._mother)
		if self._mother != other.get_mother():
			raise FieldError('这不是同一个域的多项式')
		a1 = self._deg
		b = other.get_deg()
		if a1 == -1:
			return other
		elif b == -1:
			return self
		the_answer = []
		if a1 > b:
			f1 = self._body.copy()
			g = other.get_body().copy()
		else:
			f1 = other.get_body().copy()
			g = self._body.copy()
		c = abs(a1-b)
		h = [zero]*c
		h.extend(g)
		for i in range(0, max(a1, b)+1):
			the_answer.append(f1[i] + h[i])
		return PolynomialsField(the_answer, self._mother)
	
	def __sub__(self, other):
		zero = Field_q(0, self._mother)
		if self._mother != other.get_mother():
			raise FieldError('这不是同一个域的多项式')
		a1 = self._deg
		b = other.get_deg()
		if a1 == -1:
			the_answer = other.get_body().copy()
			for i in range(0, b+1):
				the_answer[i] = zero - the_answer[i]
			return PolynomialsForFq(the_answer, other.get_mother())
		elif b == -1:
			return self
		f1 = []
		c = abs(a1 - b)
		h = [zero] * c
		if a1 >= b:
			mx = self._body.copy()
			g = other.get_body().copy()
			h.extend(g)
			for i in range(0, max(a1, b) + 1):
				f1.append(mx[i] - h[i])
			return PolynomialsForFq(f1, self._mother)
		else:
			raise FieldError('暂时还不支持这种减法')
	
	def __mul__(self, other):
		zero = Field_q(0, self._mother)
		if self._mother != other.get_mother():
			raise FieldError('这不是同一个域的多项式')
		a1 = max(self._deg, other.get_deg())
		b = min(self._deg, other.get_deg())
		if a1 == self._deg:
			mx = self._body.copy()
			g = other.get_body().copy()
		else:
			mx = other.get_body().copy()
			g = self._body.copy()
		c = a1+b
		new_coefficients = [zero]*(c+1)
		for i in range(0, b+1):
			for j in range(0, i+1):
				new_coefficients[i] += mx[i-j] * g[j]
		for i in range(b+1, a1+1):
			for j in range(0, b+1):
				new_coefficients[i] += mx[i-j] * g[j]
		for i in range(a1+1, c+1):
			for j in range(i-a1, b+1):
				new_coefficients[i] += mx[i-j] * g[j]
		return PolynomialsForFq(new_coefficients, self._mother)
	
	def the_calculate(self, x):
		degree = self._deg
		fx = self._body
		the_answer = Field_q(0, self._mother)
		for i in range(0, degree):
			the_answer += fx[i] * (x**(degree-i))
		the_answer += fx[-1]
		return the_answer
		
	def __str__(self):
		k = self._deg
		list1 = self._body.copy()
		a = list1.pop(0)
		p = self._mother
		str1 = ''
		ids = Field_q([1], p)
		zero = Field_q([0], p)
		if k > 0:
			if a == ids and k == 1:
				str1 += 'x'
				k -= 1
			elif a != ids and k == 1:
				str1 += a + '*x'
				k -= 1
			elif a == ids and k != 1:
				str1 += 'x^' + str(k)
				k -= 1
			else:
				str1 += a + 'x^' + str(k)
				k -= 1
			while k > 0:
				a = list1.pop(0)
				if a == zero:
					k -= 1
					continue
				elif a == ids and k != 1:
					str1 += '+' + 'x^' + str(k)
					k -= 1
				elif a == ids and k == 1:
					str1 += '+' + 'x'
					k -= 1
				elif a != ids and k == 1:
					str1 += '+' + str(a) + '*x'
					k -= 1
				elif a != ids and k != 1:
					str1 += '+' + str(a) + '*x^' + str(k)
					k -= 1
			a = list1[0]
			if a == zero:
				pass
			else:
				str1 += '+' + str(a)
			list1.clear()
			return str1
		elif k == 0:
			list1.clear()
			return str(self._body[0])
		elif k == -1:
			list1.clear()
			return str(0)
	
	def get_body(self):
		return self._body
	
	def get_deg(self):
		return self._deg
	
	def get_mother(self):
		return self._mother
	
	
def the_minimal(a_element):
	p = a_element.get_character()
	list1 = [a_element]
	conjugate = a_element ** p
	cnt = 0
	e = PolynomialsForFq([1], a_element.get_mother())
	zero = Field_q(0, a_element.get_mother())
	while cnt == 0:
		if conjugate == a_element:
			cnt = 1
		else:
			list1.append(conjugate)
			conjugate = conjugate ** p
	for i in range(0, len(list1)):
		e = e * PolynomialsForFq([1, zero-list1[i]], a_element.get_mother())
	return e

#
# h1 = [1, 0, 0, 0, 0, 1, 1]
# h2 = [1, 1, 0, 0, 0]
# g1 = PolynomialsField(h1, 2)
# a = Field_q(h2, g1)
# print(the_minimal(a))
