'''
前6道题的解答


from Randomness_postulates import *

f1 = PolynomialsField([1,1,0,1],2)
bases = [Field_q([1],f1),Field_q([1,0],f1),Field_q([1,0,0],f1)]
a_sequence = [[0],[1,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],
[1,0,0],[1,0,0,0],[1,0,0,0,0,0],[1,0,0,0],[0],[1,0,0,0,0],[1]]
for i in range(0 ,len(a_sequence)):
	a_sequence[i] = Field_q(a_sequence[i],f1)
for j in range(0,3):
	for i in range(0,len(a_sequence)):
		print((a_sequence[i] * bases[j]).trace(),end=',')
	print('\n')

a_list = [1,0,0,1,0,1,1,1,0,0,1,1,1,0,1,0,0]
for i in range(0,17):
	print(r3_for_2(a_list,i), end='\n')
b_list = []
a_list = [1]
for i in range(1,31):
	b_list.append((i**2)%31)
b_list = list(set(b_list))
for i in range(1,31):
	if i in b_list:
		a_list.append(0)
	else:
		a_list.append(1)
C_t = [0,1,3,5,7,11,15]
for t in C_t:
	print(r3_for_2(a_list,t),end='\n')
'''


'''
关于p143的集合的算法实现,和例题应用


def t0(list1, s, d):
	b = []
	lenth = len(list1)
	for k in range(0, int(lenth/d)):
		if isinstance(list1[k], int) and isinstance(list1[(k+s) % lenth], int):
			b.append((list1[(k+s) % lenth]-list1[k]) % d)
		elif isinstance(list1[k], str) and isinstance(list1[(k+s) % lenth], str):
			b.append('∞')
		else:
			b.append('*')
	return b


def extendshift_sequence(list1, d):
	lenth = len(list1)
	for s in range(1, d):
		for j in range(0, lenth):
			if list1[j] == '∞':
				list1.append('∞')
			else:
				list1.append((list1[j] + s) % d)
	return list1
	

the_shift_sequence = [0, 1, 4, 3, 7, '∞', 4, 1, 3, 1]
the_shift_sequence = extendshift_sequence(the_shift_sequence, 8)
for i in range(1, 9):
	d1 = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '∞': 0, '*': 0}
	d2 = t0(the_shift_sequence, i, 8)
	for it in d2:
		d1[str(it)] += 1
	print(d1)
	d1.clear()
'''


def left_shift(a,i):
	lenth = len(a)
	b = [0]*lenth
	for k in range(0,lenth):
		b[k] = a[(k+i)%lenth]
	return b
# astr = '0 1 1 0 1 0 0 1 1 0 0 0 0 1 1 1 1 0 0 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 1 0 0 1 1 0 1 1 0 0 0 0 0 0 1 0 1 1 0 0 0 1 1 0 0 1 0 0'
# astrlist = astr.split(' ')
# a = [0]*len(astrlist)
# for j in range(0, len(a)):
# 	a[j] = int(astrlist[j])
# a1 = left_shift(a, 11)
# a2 = left_shift(a, 25)
# for j in range(0, len(a)):
# 	print((a[j] + a1[j] - a2[j]) % 2, end=',')