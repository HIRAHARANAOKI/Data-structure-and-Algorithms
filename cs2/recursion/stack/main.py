# 整数を入力として受け取り、0から数値まで追加する総和計算
def simpleSummation(count):
    # ベースケース
    if count <= 0:
        return 0

    return count + simpleSummation(count-1)

print(simpleSummation(5))

