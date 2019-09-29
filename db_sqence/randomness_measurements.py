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


def games_chan(s):
	sequrnce = s
	f = PolynomialsField([1], 2)
	n = len(sequrnce)
	liner_span = 0
	b = ''
	while n > 1:
		left, right = sequrnce[:int(n/2)], sequrnce[int(n/2):]
		b = xor(left, right)
		if b == '0' * int(n/2):
			sequrnce = left
		else:
			if n == 2:
				liner_span += 2
				f = f * (PolynomialsField([1, 1], 2) ** 2)
			else:
				liner_span += int(n / 2)
				f = f * (PolynomialsField([1, 1], 2) ** int(n/2))
			sequrnce = b
		n = int(n/2)
	if b == '0' * len(b):
		return liner_span + 1
	else:
		return liner_span


# s = '0000100110101111'
# print(games_chan(s))

