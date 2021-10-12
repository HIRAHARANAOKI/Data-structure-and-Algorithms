# 素数かどうか判定する

# 素数ならtrue, 素数でないならfalseを返す
def isPrism(num):
    if num < 2:
        return False

    if num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(isPrism(1), '1') # false
print(isPrism(2), '2') # true
print(isPrism(3), '3') # true
print(isPrism(4), '4') # false
print(isPrism(25), '25') # false
print(isPrism(29), '29') # true
print(isPrism(36), '36') # false
# 出力のデータ型： bool


