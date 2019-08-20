'''
基本思路：如果a是数m的一个原根，设m的Euler函数值是e，那么a的e次方模m为1，且对任意e的因子i，a的i次方模m都不为1
通过这个思路，把m和e的所有因子作为列表输入到calculation_primitiveroot(self,p,list)中，遍历e的因子
通过判断a的i次方出现的次数是否为1次，得到一个列表，再对列表中的元素判断是否是素数，得到原根表
也可改进算法使a的i次方模m得到的所有值组成的集合，可以作为m的即约同余式，即m的即约同余式在集合中出现且只出现1次
如果确定输入的p是一个素数，则可以改进算法，对于i《=p-1的所有值，使得a的i次方模m使m的同余式中所有元素只出现一次
'''


class NumberError(Exception):       #给定错误
	
	def __init__(self):
		err = 'The number is not that i want,so i can\'t calculate it'
		Exception.__init__(self,err)


class PrimitiverootForp:
	def __init__(self):
		self.factor_list = []       #类有一个列表，用来储存类的因子
		
	def all_factor(slef, m):     #返回一个列表，包括输入m的所有因子
		list1 = []
		for i in range(1, m + 1):
			if (m / i) % 1 == 0:
				list1.append(i)
		return list1

	def calculation_primitiveroot(self,p,list):     #生成原根列表
		the_primitiveroot = []              #参照列表，装满足判断条件的所有数，可能包括合数
		the_primitiveroot_true = []         #真实列表，输出所有素数原根
		list1 = []                          #参照列表，用来
		for i in range(1, p):               #对i进行遍历
			for j in list[1:]:              #对输入的列表进行遍历，在参照列表中生成i**j的值
				list1.append((i ** j) % p)
			if list1.count(1) == 1:         #如果i是原根，则参照列表中应该包含所有p的同余项，当然值1出现的次数是1次
				the_primitiveroot.append(i)
			list1.clear()
		for i in the_primitiveroot:
			if not self.judge(i):the_primitiveroot_true.append(i)   #去掉合数
		return the_primitiveroot_true

	def judge(self,p):      #判断是否是素数，1表示不是，0表示是
		for i in range(2,p):
			if (p / i) % 1 == 0:return 1
		return 0
		
	def factor(self,m):     #通过遍历从小到大求m的第一个因子
		for i in range(2,m):
			if (m/i) % 1 == 0:
				return i

	def resulotion_into_factors(self,p):        #通过递归的方法，将p的所有因子储存在类列表中
		if not self.judge(p):           #判断是是否是素数，如果是，则分解完成
			self.factor_list.append(p)
		else:           #如果不是，那么求p最小的因子a，对p/a进行递归
			a = self.factor(p)
			self.factor_list.append(a)
			self.resulotion_into_factors(int(p/a))

	def euler_function(self, p):         #给出p的Euler函数值，必须先经过resulotion_into_factors属性
		if len(self.factor_list) == 1:
			return self.factor_list[0]-1      #类列表里面只有一个即输入是素数p，返回p-1
		self.factor_list = list(set(self.factor_list))      #把p的因子分解去重
		k = p
		for i in self.factor_list:      #合数Euler函数算法
			k = (k*(i-1))/i
		return int(k)
	
	def judge_conditions(self,p):       #判断输入的p是否是符合原根存在条件，如果不符合则引发错误
		if len(self.factor_list) == 1:
			pass
		else:
			a = self.factor_list[0]
			b = self.factor_list[1]
			len_for_factor = len(self.factor_list)
			len_for_b = self.factor_list.count(b)
			if p == 1 or p == 2 or p == 4:
				pass
			elif a == 2 and (len_for_b ==(len_for_factor-1)):
				pass
			elif len_for_factor == len_for_b:
				pass
			else:
				raise NumberError

	def rush_duck(self, p):
		self.factor_list.clear()        #重置类列表
		self.resulotion_into_factors(p) #列表中储存p的所有因子
		self.judge_conditions(p)        #判断p是否满足条件
		e = self.euler_function(p)      #列表去重，并且返回Euler函数值
		list1 = self.all_factor(e)       #包含Euler函数值的所有因子
		return self.calculation_primitiveroot(p, list1)       #生成原根列表


def gcd(a, b):
	if b > a:
		a, b = b, a
	if b == 0:
		return a
	else:
		return gcd(b, a % b)


def eular_function(q):
	the_eular_list = []
	for i in range(0, q):
		if gcd(q, i) == 1:
			the_eular_list.append(i)
	return the_eular_list

# b = PrimitiverootForp()
# list1 = b.rush_duck(8)
# print(list1)
