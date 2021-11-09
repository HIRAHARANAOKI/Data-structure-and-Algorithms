import math


def countSquare(x, y):
	num = gcd(x, y)
	# result = (x * y) / (num * num)
	result = x * y / math.pow(num, 2)
	print(result)


def gcd(m, n):
	if (m % n) == 0:
		return n
	else:
		return gcd(n, m % n)


countSquare(28, 32)
