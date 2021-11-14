import  math
# 約数
# 天才小学生の Julia ちゃんは学校で出された約数を求める問題に対して
# 1 問 1 問素因数分解するのが面倒に感じたため、独自でプログラムを開発することにしました。
# ある数値 number が与えられるので、number の約数を小さい順に返す
# divisor という関数を再帰を使って定義してください。

def divisor(num):
	return divisorHelper(num, num, "")

def divisorHelper(num, count, string):
	print(num, count, string)

	return divisorHelper()
	# if count <= 1:
	# 	return ""
	#
	# if num%count == 0:
	# 	return str(num/count) + "-"
	#
	# return	divisorHelper(num, count-1, string)



print(divisor(6))
# 6/6 ① 1-
# 6/3 ② 1-2-
# 6/2 ③ 1-2-3-
# 6/1 ④ 1-2-3-6


# print(divisor(28))
# 28/28
# 28/14
# 28/7
# 28/4
# 28/2
# 28/1


# print(divisor(29))

# divisor(28) --> 1-2-4-7-14-28
# divisor(29) --> 1-29
# divisor(720) --> 1-2-3-4-5-6-8-9-10-12-15-16-18-20-24-30-36-40-45-48-60-72-80-90-120-144-180-240-360-720