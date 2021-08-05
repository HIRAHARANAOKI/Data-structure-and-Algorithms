# 文字列の長さをカウントする
def lengthString(string):
    if string == "":
        return 0
    return 1 + lengthString(string[1:])

# 5
print(lengthString("hello"))