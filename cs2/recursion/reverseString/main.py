def reversedStringHelper(reversedString, leftString):
    if len(leftString) <= 0:
        return reversedString
    print('left[0]+reversed:',leftString[0] + reversedString, 'left:[1:]',leftString[1:])
    return reversedStringHelper(leftString[0] + reversedString , leftString[1:])

def reversedString(string):
    return reversedStringHelper(string[0], string[1:])

reversedString('abcd')
# print(reversedString('RareTECH'))


