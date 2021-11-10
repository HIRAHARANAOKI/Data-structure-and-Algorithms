# 3で割り続ける
# 3 の累乗 n が与えられるので、整数 n を 3 で除算できる回数を返す、divideBy3Count という関数を作成してください。

def divideBy3Count(n):
	return divideBy3CountHelper(n, 0)


def divideBy3CountHelper(n, count):
	print('n:', n, 'count:', count)
	if n <= 1:
		return count

	return divideBy3CountHelper(n / 3, count + 1)


print(divideBy3Count(1))  # 0
print(divideBy3Count(3))  # 1
print(divideBy3Count(27))  # 3
print(divideBy3Count(729))  # 6
