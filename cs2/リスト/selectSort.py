arr = [34,446,32,3,2,8,6,76,56,45,34,56,1]

def selectSort(list):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if list[j] < list[min]:
                min = j

        temp = list[i]
        list[i] = list[min]
        list[min] = temp


print(arr)
selectSort(arr)
print(arr)


insertarr = [34,446,32,3,2,8,6,76,56,45,34,56,1]
def insertionSort(arrList):
    n = len(arrList)
    # 配列を左から右へと処理します。
    for i in range(n):
        # currentValueは配列の左端に挿入される項目です。
        currentValue = arrList[i]
        # jは右から左へインデックスを追跡します。左側にあるものはすべてソートされています。
        for j in range(i - 1, -1, -1):
            # もし、currentValueが小さい場合は、左右の値を入れ替えます。
            if currentValue <= arrList[j]:
                arrList[j+1] = arrList[j]
                arrList[j] = currentValue
            # 現在の値がA[j]よりも大きい場合、それは正しい位置にあるので、ループを終了してi+1に移動します。
            else: break

# print(insertarr)
# insertionSort(insertarr) # 昇順に並び替え
# print(insertarr) # ソートされた配列
