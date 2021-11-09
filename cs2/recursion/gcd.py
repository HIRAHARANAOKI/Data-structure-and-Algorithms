# def gcd(m, n) :
#     if m == n :
#         return m
#     elif m > n :
#         return gcd(m-n,n)
#     else:
#         return gcd(m,n-m)


# 上記の処理よりもmodを使うことで計算量は少なくなる
def gcd(m, n):
    if (m%n)==0:
        return n
    else:
        return gcd(n, m%n)
# 44と242の最大公約数を求める
print(gcd(44,242))

# この計算も
gcd (60,168)
= gcd (60,168-60) = gcd (60,108)
= gcd (60,108-60) = gcd (60,48)

# これをmodを用いると？
gcd (60,168)
= gcd (60, 168 mod 60) = gcd (60,48)