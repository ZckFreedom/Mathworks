from A_new_way_of_P_Field import *


class FieldError(ValueError):
	pass


'''
先类似之前的方式定义一个域，每个实例都是一个域
然后定义一个多项式域，每个实例是一个列表或者数组，列表之间的计算需要根据需要进行定义
最后定义一个判断函数，如果多项式域中的一个实例的每个元素都是在域的一个实例中，那么称这个多项式属于这个域
'''

# class ModPField:
# 	@staticmethod
# 	def judge(p):
# 		if isinstance(p,int):
# 			for i in range(2,p):
# 				if p%i ==0:
# 					return False
# 			return True
#
# 	def __init__(self,p):
# 		if ModPField.judge(p):
# 			self._module = p


# def inverseP(a,b,p):
# 	for i in range(1, p):
# 		if (b * i) % p == a:
# 			return i
# 	return 0
	
'''
class PolynomialsField:
	# 多项式的系数用列表表示，采用幂次从大到小的方式
	def __init__(self,list1,p):
		list2 = []
		for i in range(len(list1)): #如果输入的列表中有0的话，则先把列表最前面的0去掉
			if list1[i] ==0 and len(list2)==0:continue  #因为这些0在多项式中没有意义
			list2.append((list1[i])%p)
		if len(list2) == 0:list2 =[0]
		self._coefficients = list2
		self._deg = len(list2)-1
		self._mod = p
	
	def __str__(self):  #将实例作为多项式表示出去
		k = self._deg
		list1= self._coefficients.copy()
		a = list1.pop(0)
		str1 = ''
		if k > 0:
			if a ==1 and k==1:
				str1 += 'x'
				k -=1
			elif a!=1 and k==1:
				str1 += str(a) + '*x'
				k -=1
			elif a==1 and k!=1:
				str1 += 'x^' + str(k)
				k -=1
			else:
				str1 += str(a) + 'x^' + str(k)
				k -=1
			while k > 0:
				a = list1.pop(0)
				if a==0:
					k -=1
					continue
				elif a ==1 and k!=1:
					str1 += '+' + 'x^' + str(k)
					k -=1
				elif a ==1 and k==1:
					str1 += '+' + 'x'
					k -= 1
				elif a!=1 and k==1:
					str1 +=  '+'+ str(a) + '*x'
					k -= 1
				elif a!=1 and k!=1:
					str1 += '+' + str(a) + '*x^' + str(k)
					k -=1
			a = list1[0]
			if a==0:pass
			else:
				str1 += '+' + str(a)
			list1.clear()
			return str1
		elif k ==0:
			list1.clear()
			return str(self._coefficients[0])
	
	def __add__(self, other):   #定义多项式的加法
		if self._mod != other._mod:
			raise FieldError('这不是同一个域的多项式')
		p = self._mod
		new_coefficients = []
		if self._deg < other._deg:
			k = other._deg - self._deg
			t = [0] *k
			t.extend(self._coefficients)
			for i in range(len(t)):
				new_coefficients.append((t[i] + other._coefficients[i]) %p)
		elif self._deg > other._deg:
			k = self._deg - other._deg
			t = [0] * k
			t.extend(other._coefficients)
			for i in range(len(t)):
				new_coefficients.append((t[i] + self._coefficients[i]) %p)
		else:
			for i in range(len(self._coefficients)):
				new_coefficients.append((self._coefficients[i] + other._coefficients[i]) %p)
		return PolynomialsField(new_coefficients,p)
	
	def __sub__(self, other):   #定义多项式的减法
		if self._mod != other._mod:
			raise FieldError('这不是同一个域的多项式')
		p = self._mod
		new_coefficients = []
		if self._deg < other._deg:
			k = other._deg - self._deg
			t = [0] *k
			t.extend(self._coefficients)
			for i in range(len(t)):
				new_coefficients.append((t[i] - other._coefficients[i]) %p)
		elif self._deg > other._deg:
			k = self._deg - other._deg
			t = [0] * k
			t.extend(other._coefficients)
			for i in range(len(t)):
				new_coefficients.append((t[i] - self._coefficients[i]) %p)
		else:
			for i in range(len(self._coefficients)):
				new_coefficients.append((self._coefficients[i] - other._coefficients[i]) %p)
		return PolynomialsField(new_coefficients,p)
	
	def __mul__(self, other):
		p = self._mod
		if self._mod != other._mod:
			raise FieldError('这不是同一个域的多项式')
		if self._coefficients ==[0] or other._coefficients ==[0]:
			return PolynomialsField([0],p)
		else:
			k = self._deg + other._deg+1
			new_coefficients = [0]*k
			for i in range(len(new_coefficients)):
				t = min(len(self._coefficients),i+1)
				for j in range(t):
					m = i-j
					if m<len(other._coefficients):
						new_coefficients[i] += (self._coefficients[j] * other._coefficients[m])%p
		return PolynomialsField(new_coefficients,p)
	
	def __mod__(self, other):
		p = self._mod
		if other._coefficients == [0]:
			raise FieldError('被余多项式错误')
		if self._mod != other._mod:
			raise FieldError('这不是同一个域的多项式')
		if self._deg < other._deg:
			return self
		elif self._deg == other._deg:
			a = self._coefficients[0]
			b = other._coefficients[0]
			c = inverseP(a,b,p)
			if c==0:raise FieldError('两个多项式不能求余')
			else:
				return (self - PolynomialsField([c],p) * other)
		elif self._deg > other._deg:
			k = self._deg - other._deg
			a = self._coefficients[0]
			b = other._coefficients[0]
			c = 0
			for i in range(1, p):
				if (b * i) % p == a:
					c = i
					break
			if c == 0: raise FieldError('两个多项式不能求余')
			else:
				list1 = other._coefficients.copy()
				list1.extend([0]*k)
				another =  self - PolynomialsField([c],p) * PolynomialsField(list1,p)
				if another._deg < other._deg:
					return another
				else:
					return another % other
	
	def __truediv__(self, other):
		p = self._mod
		if self._mod != other._mod:
			raise FieldError('这不是同一个域的多项式')
		mod = (self%other)._coefficients
		if mod !=[0]:
			raise FieldError('不能整除')
		if other._coefficients == [0]:
			raise FieldError('被除多项式错误')
		factor = [0] *(self._deg - other._deg +1)
		deg_factor = len(factor)
		f = PolynomialsField(self._coefficients.copy(),p)
		g = PolynomialsField(other._coefficients.copy(),p)
		while f._coefficients != [0]:
			k = f._deg - g._deg
			a = f._coefficients[0]
			b = g._coefficients[0]
			c = inverseP(a,b,p)
			factor[deg_factor - k -1] = c
			list1 = g._coefficients.copy()
			list1.extend([0] * k)
			h = f - PolynomialsField(list1,p) * PolynomialsField([c],p)
			f = PolynomialsField(h._coefficients.copy(),p)
			h._coefficients.clear()
		return PolynomialsField(factor,p)
	
	def is_irreducible(self):
		p = self._mod
		k = self._deg //2 +1
		for i in range_pofn(p,k):
			f = PolynomialsField(i,p)
			if f._deg ==0:
				continue
			else:
				mod = (self % f)._coefficients
				if mod == [0]:
					print(self,'是可约多项式')
					return
		print(self,'是不可约多项式')
		return
	
	def caculate(self,a):
		sum1 = 0
		k = self._deg +1
		p = self._mod
		for i in range(k):
			sum1 += (self._coefficients[k] * (a**(k-1-i)))%p
		return sum1%p
	
	def is_zero(self,a):
		return self.caculate(a)==0


class FqField:
	def __init__(self,f,p,i,a):
		if not isinstance(f,PolynomialsField) or not isinstance(a,str):
			raise FieldError
		self._mod = p
		self._respect = a
		self._power = i
		list1 = [1]
		list1.extend([0] * i)
		self._polynomial = PolynomialsField(list1,p)%f
	
	def __str__(self):
		k = self._polynomial._deg
		list1 = self._polynomial._coefficients.copy()
		t = self._respect
		a = list1.pop(0)
		str1 = ''
		if k > 0:
			if a == 1 and k == 1:
				str1 += t
				k -= 1
			elif a != 1 and k == 1:
				str1 += str(a) + '*' + t
				k -= 1
			elif a == 1 and k != 1:
				str1 += t + '^' + str(k)
				k -= 1
			else:
				str1 += str(a) + t + '^' + str(k)
				k -= 1
			while k > 0:
				a = list1.pop(0)
				if a == 0:
					k -= 1
					continue
				elif a == 1 and k != 1:
					str1 += '+' + t + '^' + str(k)
					k -= 1
				elif a == 1 and k == 1:
					str1 += '+' + t
					k -= 1
				elif a != 1 and k == 1:
					str1 += '+' + str(a) + '*' + t
					k -= 1
				elif a != 1 and k != 1:
					str1 += '+' + str(a) + '*^' + t + str(k)
					k -= 1
			a = list1[0]
			if a == 0:
				pass
			else:
				str1 += '+' + str(a)
			list1.clear()
			return str1
		elif k == 0:
			list1.clear()
			return str(self._polynomial._coefficients[0])
'''


class PolynomialsField:
	# 初始化函数，将给定的一个列表的前面的0消去
	@staticmethod
	def initialize(list1):
		if isinstance(list1, int):
			return [list1]
		if len(list1) == 0:
			return [0]
		if isinstance(list1[0], int):
			for i in range(0, len(list1)):
				if list1[i] != 0:
					return list1[i:]
		elif isinstance(list1[0], Field_p):
			for i in range(0, len(list1)):
				if list1[i].get_body() != 0:
					return list1[i:]
		return [0]
	
	# 数乘函数，计算一个数和一个多项式的数乘
	@staticmethod
	def multiplication(c, list1):
		if len(list1) == 0:
			return [0]
		for i in range(0, len(list1)):
			list1[i] = c * list1[i]
		return list1
	
	# 生成序列，p域中次数小于n的所有可能的多项式
	@staticmethod
	def range_p_of_n(p, n):
		zero = Field_p(0, p)
		list1 = [zero] * n
		cnt = 0
		while cnt < (p ** n):
			for j in range(n):
				a = cnt // (p ** (n - 1 - j))
				list1[j] = Field_p(a, p)
			cnt += 1
			yield PolynomialsField(list1, p)
	
	# 列表计算，返回列表
	@staticmethod
	def sub_for_list(list1, list2):
		n = len(list1) - len(list2)
		zero = Field_p(0, list1[0].get_home())
		h = [zero] * n
		f = list1.copy()
		g = list2.copy()
		g.extend(h)
		a = f[0]
		b = g[0]
		c = a/b
		g = PolynomialsField.multiplication(c, g)
		for i in range(0, len(list1)):
			f[i] = f[i] - g[i]
		return f
		
	def __init__(self, list1, p):
		list2 = PolynomialsField.initialize(list1)
		self._body = []
		for i in range(0, len(list2)):
			self._body.append(Field_p(list2[i], p))
		if len(list2) == 1:
			if isinstance(list2[0], int) and list2[0] == 0:
				self._deg = -1
			elif isinstance(list2[0], Field_p) and list2[0].get_body() == 0:
				self._deg = -1
			else:
				self._deg = len(list2) - 1
		else:
			self._deg = len(list2) - 1
		self._home = p
	
	def __add__(self, other):
		zero = Field_p(0, self._home)
		if self._home != other.get_home():
			raise FieldError('这不是同一个域的多项式')
		a = self._deg
		b = other.get_deg()
		if a == -1:
			return other
		elif b == -1:
			return self
		f1 = []
		if a > b:
			f = self._body.copy()
			g = other.get_body().copy()
		else:
			f = other.get_body().copy()
			g = self._body.copy()
		c = abs(a-b)
		h = [zero]*c
		h.extend(g)
		for i in range(0, max(a, b)+1):
			f1.append(f[i] + h[i])
		return PolynomialsField(f1, self._home)
	
	def __sub__(self, other):
		zero = Field_p(0, self._home)
		if self._home != other.get_home():
			raise FieldError('这不是同一个域的多项式')
		a = self._deg
		b = other.get_deg()
		if a == -1:
			f = other.get_body().copy()
			for i in range(0, b+1):
				f[i] = zero-f[i]
			return PolynomialsField(f, other.get_home())
		elif b == -1:
			return self
		f1 = []
		c = abs(a - b)
		h = [zero] * c
		if a >= b:
			f = self._body.copy()
			g = other.get_body().copy()
			h.extend(g)
			for i in range(0, max(a, b) + 1):
				f1.append(f[i] - h[i])
			return PolynomialsField(f1, self._home)
		else:
			raise FieldError('暂时还不支持这种减法')
	
	def __mul__(self, other):
		zero = Field_p(0, self._home)
		if self._home != other.get_home():
			raise FieldError('这不是同一个域的多项式')
		a = max(self._deg, other.get_deg())
		b = min(self._deg, other.get_deg())
		p = self._home
		if a == self._deg:
			f = self._body.copy()
			g = other.get_body().copy()
		else:
			f = other.get_body().copy()
			g = self._body.copy()
		c = a+b
		new_coefficients = [zero]*(c+1)
		for i in range(0, b+1):
			for j in range(0, i+1):
				new_coefficients[i] += f[i-j] * g[j]
		for i in range(b+1, a+1):
			for j in range(0, b+1):
				new_coefficients[i] += f[i-j] * g[j]
		for i in range(a+1, c+1):
			for j in range(i-a, b+1):
				new_coefficients[i] += f[i-j] * g[j]
		return PolynomialsField(new_coefficients, p)
	
	def __eq__(self, other):
		if self._home != other.get_home():
			raise FieldError('这不是同一个域的多项式')
		a = self._deg + 1
		b = other.get_deg() + 1
		if a != b:
			return False
		try:
			for i in range(0, a):
				if self._body[i] == other.get_body()[i]:
					pass
				else:
					return False
		except IndexError:
			return False
		return True
	
	def __mod__(self, other):
		if self._home != other.get_home():
			raise FieldError('这不是同一个域的多项式')
		if other.get_body() == [Field_p(0, other.get_home())]:
			raise FieldError('不能求余')
		a = self._deg
		b = other.get_deg()
		f = self._body.copy()
		g = other.get_body().copy()
		p = self._home
		if a < b:
			return self
		else:
			new_polynomial = []
			while a >= b:
				new_coefficients = PolynomialsField.sub_for_list(f, g)
				new_polynomial = PolynomialsField(new_coefficients, p)
				a = new_polynomial._deg
				f = new_polynomial._body
			return new_polynomial
	
	def __truediv__(self, other):
		zero = PolynomialsField([0], self._home)
		zero_element = Field_p(0, self._home)
		if self._home != other.get_home():
			raise FieldError('这不是同一个域的多项式')
		if other == zero:
			raise FieldError('被除多项式错误')
		if not self % other == zero:
			raise FieldError('不能整除')
		deg_factor = (self._deg - other.get_deg() + 1)
		factor = [zero] * deg_factor
		p = self._home
		f = PolynomialsField(self._body.copy(), p)
		g = PolynomialsField(other.get_body().copy(), p)
		while not f == zero:
			k = f._deg - g._deg
			a = f._body[0]
			b = g._body[0]
			c = a/b
			factor[deg_factor - k - 1] = c
			list1 = g._body.copy()
			list1.extend([zero_element] * k)
			h = PolynomialsField(list1, p) * PolynomialsField([c], p)
			f = f - PolynomialsField(h._body.copy(), p)
			h._body.clear()
		return PolynomialsField(factor, p)
	
	def is_irreducible(self):
		p = self._home
		zero = PolynomialsField([0], p)
		k = self._deg // 2 + 1
		for i in PolynomialsField.range_p_of_n(p, k):
			f = i
			if f._deg == -1 or f._deg == 0:
				continue
			else:
				mod = (self % f)
				if mod == zero:
					# print(self, '是可约多项式')
					return False
		# print(self, '是不可约多项式')
		return True
	
	def __str__(self):
		k = self._deg
		list1 = self._body.copy()
		a = list1.pop(0)
		p = self._home
		str1 = ''
		ids = Field_p(1, p)
		zero = Field_p(0, p)
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
		
	def __pow__(self, n):
		p = self.get_home()
		func_h = PolynomialsField([1], p)
		while n > 0:
			func_h *= self
			n -= 1
		return func_h
	
	def order(self):
		n = self._deg
		p = self._home
		zero = PolynomialsField([0], p)
		while True:
			list1 = [0] * (n - 1)
			list2 = [1]
			list2.extend(list1)
			list2.append(-1)
			f = PolynomialsField(list2, p)
			if f % self == zero:
				return n
			n += 1
			list1.clear()
			list2.clear()
	
	def get_body(self):
		return self._body
	
	def get_deg(self):
		return self._deg
	
	def get_home(self):
		return self._home


# h1 = [1,1,0,0,0,1,0,1,1]
# h2 = [1,1,1]
# h1 = [1,1,1]
# g1 = PolynomialsField(h1,2)
# h2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# g2 = PolynomialsField(h2,2)
# # print(g1%g2)
# g1.is_irreducible()
# print(g1.order())
# print(g2)
# g1 *=g1
# print(g1)
