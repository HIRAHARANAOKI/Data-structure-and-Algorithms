# 3回以上欠席すると、単位を取得できない制度

def doYouFail(string):
    return 'fail' if string.count("A") >= 3 else 'pass'

print(doYouFail("AAPPAP"), 'fail')
print(doYouFail("AAPPAA"), 'fail')
print(doYouFail("PAPPA"), 'pass')
# 入力のデータ型： string string
# 出力のデータ型： string