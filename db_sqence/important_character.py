from Polynomials_Field import PolynomialsField


def xor(s1, s2):
	n = len(s1)
	b = ''
	for i in range(0, n):
		if s1[i] == s2[i]:
			b += '0'
		else:
			b += '1'
	return b


def games_chan(db):
	"""
	求db序列的线性复杂度
	"""
	sequence = db
	f = PolynomialsField([1], 2)
	n = len(sequence)
	liner_span = 0
	b = ''
	while n > 1:
		left, right = sequence[:int(n/2)], sequence[int(n/2):]
		b = xor(left, right)
		if b == '0' * int(n/2):
			sequence = left
		else:
			if n == 2:
				liner_span += 2
				f = f * (PolynomialsField([1, 1], 2) ** 2)
			else:
				liner_span += int(n / 2)
				f = f * (PolynomialsField([1, 1], 2) ** int(n/2))
			sequence = b
		n = int(n/2)
	if b == '0' * len(b):
		return liner_span + 1
	else:
		return liner_span


def find_n0(s1):
	for i in range(len(s1)):
		if int(s1[i]) == 1:
			return i


def find_m(lc_list):
	ln = lc_list[-1]
	for i in range(len(lc_list)-1, -1, -1):
		if lc_list[i] != ln:
			return i


def ply_add(l1, l2):
	a = len(l1)
	b = len(l2)
	add_ply = []
	if a > b:
		c = a-b
		l3 = [0]*c
		l3 += l2
		for i in range(a):
			add_ply.append((l1[i] + l3[i]) % 2)
	elif a < b:
		c = b-a
		l3 = [0] * c
		l3 += l1
		for i in range(b):
			add_ply.append((l1[i] + l3[i]) % 2)
	else:
		for i in range(b):
			add_ply.append((l1[i] + l2[i]) % 2)
	if add_ply[0] == 0:
		add_ply.pop(0)
	return add_ply


def b_m(sequence):
	"""
	求一般序列线性复杂度的BM算法
	"""
	N = len(sequence)
	mpl = []
	lcl = []
	n = find_n0(sequence)
	mp = [1]
	mp += [0]*int(n)
	mp += [1]
	for i in range(n):
		mpl.append([1])
		lcl.append(0)
	mpl.append(mp.copy())
	lcl.append(n+1)
	while n < N-1:
		n += 1
		d = 0
		for i in range(len(mp)):
			d += mp[i] * int(sequence[n-i])
		if d % 2 == 0:
			mpl.append(mpl[-1].copy())
			lcl.append(lcl[-1])
		elif d % 2 == 1:
			m_1_index = find_m(lcl)
			if m_1_index == 0:
				k = 1-n+lcl[-1]
			else:
				k = m_1_index+1-lcl[m_1_index]-n+lcl[-1]
			if k >= 0:
				mpm = mpl[m_1_index] + [0]*k
				mp = ply_add(mp, mpm)
				mpl.append(mp.copy())
				lcl.append(lcl[-1])
			elif k < 0:
				mp += [0] * int(-k)
				mp = ply_add(mp, mpl[m_1_index])
				mpl.append(mp.copy())
				lcl.append(n+1-lcl[-1])
	return mpl[-1], lcl[-1]


# s = '000001111110101011010010100010111011000110010000100110111100111000001111110101011010010100010111011000110010000100110111100111'
# # print(games_chan(s))
# print(b_m(s))
