def reverseStringHelper(reversedString, leftString):

    # ベースケース
    if len(leftString) <= 0:
        return reversedString

    # print(reversedString, 'reversedString')
    # print(leftString, 'leftString')

    return reverseStringHelper(leftString[0] + reversedString, leftString[1:])

def reverseString(string):
   return reverseStringHelper(string[0], string[1:])


s = "abcd"
print(reverseString(s))


# 入出力
# "abcd" → ""
# "abc" → "d"
