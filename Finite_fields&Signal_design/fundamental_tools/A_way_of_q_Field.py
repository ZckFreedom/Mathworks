from Polynomials_Field import *

'''
以1，θ，θ^2等为基，定义了基本运算，以及求逆等运算
'''


class Field_q:
	def __init__(self, list1, h):
		if not isinstance(h, PolynomialsField):
			raise FieldError('定义错误')
		if not h.is_irreducible():
			raise FieldError('f不是不可约，不是域')
		p = h.get_home()
		if isinstance(list1, int):
			if list1 == 0:
				self._body = PolynomialsField([0], p)
			else:
				g = PolynomialsField(list1, p)
				self._body = g % h
		elif isinstance(list1[0], int):
			if list1 == [0]:
				self._body = PolynomialsField([0], p)
			else:
				g = PolynomialsField(list1, p)
				self._body = g % h
		elif isinstance(list1, PolynomialsField):
			if list1 == PolynomialsField([0], p):
				self._body = PolynomialsField([0], p)
		else:
			g = PolynomialsField(list1, p)
			self._body = g % h
		self._character = p
		self._mother = h
		
	def __add__(self, other):
		if self._mother != other.get_mother():
			raise FieldError('不是一个域中的元素')
		p = self._character
		h = self._body.get_body().copy()
		g = other.get_body().get_body().copy()
		new_polynomial = PolynomialsField(h, p) + PolynomialsField(g, p)
		new_coefficients = new_polynomial.get_body().copy()
		return Field_q(new_coefficients, self._mother)
	
	def __sub__(self, other):
		if self._mother != other.get_mother():
			raise FieldError('不是一个域中的元素')
		p = self._character
		h = self._body.get_body().copy()
		g = other.get_body().get_body().copy()
		new_polynomial = PolynomialsField(h, p) - PolynomialsField(g, p)
		new_coefficients = new_polynomial.get_body().copy()
		return Field_q(new_coefficients, self._mother)
	
	def __mul__(self, other):
		if self._mother != other.get_mother():
			raise FieldError('不是一个域中的元素')
		p = self._character
		h = self._body.get_body().copy()
		g = other.get_body().get_body().copy()
		new_polynomial = PolynomialsField(h, p) * PolynomialsField(g, p)
		new_coefficients = new_polynomial.get_body().copy()
		return Field_q(new_coefficients, self._mother)
	
	def __eq__(self, other):
		if self._mother != other.get_mother():
			raise FieldError('不是一个域中的元素')
		return self._body == other.get_body()
	
	def __pow__(self, p):
		r = self._mother
		g = Field_q([1], r)
		h = Field_q(self._body.get_body().copy(), r)
		while p > 0:
			g *= h
			p -= 1
		return g
	
	def ord(self):
		if self == Field_q([0], self.get_mother()):
			return 0
		r = self._mother
		ids = Field_q([1], r)
		h = Field_q(self._body.get_body().copy(), r)
		g = Field_q([1], r)
		n = 1
		while True:
			g = g * h
			if g == ids:
				return n
			n += 1

	def inverse(self):
		r = self._mother
		h = Field_q(self._body.get_body().copy(), r)
		g = Field_q([1], r)
		n = self.ord()
		while n > 1:
			g = g * h
			n -= 1
		return g
	
	def __truediv__(self, other):
		the_inverse = self.inverse()
		return other*the_inverse
	
	def get_mother(self):
		return self._mother
	
	def get_body(self):
		return self._body
	
	def get_character(self):
		return self._character
	
	def trace(self):
		n = self.get_mother().get_deg()
		p = self._character
		h = Field_q([0], self.get_mother())
		g = Field_q(self._body.get_body().copy(), self.get_mother())
		while n > 0:
			h += g
			g = g**p
			n -= 1
		return h
	
	def __str__(self):
		k = self.get_body().get_deg()
		list1 = self.get_body().get_body().copy()
		a = list1.pop(0)
		p = self.get_body().get_home()
		str1 = ''
		ids = Field_p(1, p)
		zero = Field_p(0, p)
		if k > 0:
			if a == ids and k == 1:
				str1 += 'θ'
				k -= 1
			elif a != ids and k == 1:
				str1 += str(a) + '*θ'
				k -= 1
			elif a == ids and k != 1:
				str1 += 'θ^' + str(k)
				k -= 1
			else:
				str1 += str(a) + 'θ^' + str(k)
				k -= 1
			while k > 0:
				a = list1.pop(0)
				if a == zero:
					k -= 1
					continue
				elif a == ids and k != 1:
					str1 += '+' + 'θ^' + str(k)
					k -= 1
				elif a == ids and k == 1:
					str1 += '+' + 'θ'
					k -= 1
				elif a != ids and k == 1:
					str1 += '+' + str(a) + '*θ'
					k -= 1
				elif a != ids and k != 1:
					str1 += '+' + str(a) + '*θ^' + str(k)
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
			return str(self._body.get_body()[0])
		elif k == -1:
			list1.clear()
			return str(0)

		
# h1 = [1, 0, 0, 1, 1]
# h2 = [1, 0]
# g1 = PolynomialsField(h1, 2)
# # print(g1.is_irreducible())
# f = Field_q(h2, g1)
# # print(f.trace().get_body())
# sequence_a = [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0]
# for k in range(0, len(sequence_a)):
# 	sequence_a[k] = Field_q(sequence_a[k], g1)
# for k in range(0, len(sequence_a)):
# 	g = Field_q([0], g1)
# 	for t in range(0, len(sequence_a)):
# 		g += sequence_a[t] * f**(t*k)
# 	print(g)
#
# print(f)
