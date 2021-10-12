import  random

intArr = [0, 1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
print(intArr)

for i in range(len(intArr)):
    j = random.randint(i, len(intArr) -1)

    temp = intArr[i]
    intArr[i] = intArr[j]
    intArr[j] = temp
    print(intArr, 'intArr', j, 'j')

print(intArr)
