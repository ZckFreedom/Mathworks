from primitiverootForp import gcd


def super_order(k, q):
	the_sum = 1
	t = 1
	while the_sum % q != 0 or the_sum == 1:
		the_sum += k**t
		t += 1
	return t


def order(k, q):
	t = 1
	while (k**t) % q != 1 or t == 1:
		t += 1
	return t


# b = order(14, 15)
# a = super_order(14, 15)
# print(b, a)
def all_order(n):
	for k in range(2, n):
		if gcd(k, n) == 1:
			print(k, order(k, n), super_order(k, n))

