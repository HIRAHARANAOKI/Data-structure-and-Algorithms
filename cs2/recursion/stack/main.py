# 整数を入力として受け取り、0から数値まで追加する総和計算
def simpleSummation(count):
    # ベースケース
    if count <= 0:
        return 0

    return count + simpleSummation(count-1)

print(simpleSummation(5)) #15

# 3 までの総和を計算
# simpleSummation(3)
# 3 + simpleSummation(2)
# 3 + (2 + simpleSummation(1))
# 3 + (2 + (1 + simpleSummation(0)))
# 3 + (2 + (1 + 0))
# 3 + (2 + 1)
# 3 + 3
# 6

