# 文字列の長さをカウントする
def lengthString(string):
    if string == "":
        return 0
    return 1 + lengthString(string[1:])

print(lengthString("hello")) # 5