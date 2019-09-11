from primitiverootForp import gcd


def super_order(k, q):
	if q == 1:
		return 1
	the_sum = 1
	t = 1
	while the_sum % q != 0 or the_sum == 1:
		the_sum += k**t
		t += 1
	return t


def order(k, q):
	if q == 1:
		return 1
	t = 1
	while (k**t) % q != 1 or t == 1:
		t += 1
	return t


# b = order(28, 255)
# a = super_order(28, 255)
# print(a, b)


def all_order(n):
	for k in range(2, n):
		if gcd(k, n) == 1:
			a, b, c = gcd(k-1, n), order(k, n), super_order(k, n)
			if c == (a*b):
				print(k, 'gcd:', a, 'order:', b, 'super_order:', super_order(k, n), 'test:', a * b)
			elif b == c:
				print(k, 'gcd:', a, 'order:', b, 'super_order:', super_order(k, n), 'test:', a * b, '*')
			elif a == c:
				print(k, 'gcd:', a, 'order:', b, 'super_order:', super_order(k, n), 'test:', a * b, '**')
			else:
				print(k, 'gcd:', a, 'order:', b, 'super_order:', super_order(k, n), 'test:', a * b, '***')


def all_order1(n):
	for k in range(2, n):
		if gcd(k, n) == 1:
			a, b, c = gcd(k-1, n), order(k, n), super_order(k, n)
			n1 = n/a
			number1 = (k**b - 1)/(k - 1)
			number2 = number1/n1
			number3 = gcd(number2, a)
			number5 = int(a/number3)
			# e = super_order(number4, number5)
			# print(k, 'gcd:', a, 'order:', b, 'super_order:', c, 'test:', e * b)
			if number5 == int(c/b) or c == a*b:
				pass
			else:
				print(k, 'gcd:', a, 'order:', b, 'super_order:', c, 'test:', number5 * b)


all_order1(342)
# 工具