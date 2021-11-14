# 例題 【チャレンジ問題】

# 今n段の階段があり、この階段では1ステップで1段、および2段しか登ることができません
# 階段の頂上まで到達するまでのステップが何通りあるか数えるnumberOfWaysという関数を作成してください
# 例えば、n=3の時、頂上に到達するには、1+1+1、1+2、2+1の3通りが存在します
# n=4の時、1+1+1+1、1+2+1、1+1+2、2+1+1、2+2の5通りが存在します
# 5 → 8 # 10 → 89 # 20 → 10946


def numberOfWays(n):
	if n == 1:
		return 1
	if n == 2:
		return 2
	return numberOfWays(n - 1) + numberOfWays(n - 2)


print(numberOfWays(1))  # 1
print(numberOfWays(2))  # 2
print(numberOfWays(3))  # 3
print(numberOfWays(4))  # 5
print(numberOfWays(5))  # 8




