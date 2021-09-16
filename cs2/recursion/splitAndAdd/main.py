import math

def splitAndAdd(digits):
    return splitAndAddHelper(digits, 0)

def splitAndAddHelper(digits, sum):
    if digits <= 0:
        return sum
    return splitAndAddHelper(digits/10, sum + math.floor(digits%10))
print(splitAndAdd(19))


# aaa
