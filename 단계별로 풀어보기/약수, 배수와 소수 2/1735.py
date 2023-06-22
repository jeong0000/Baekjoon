'''
분수 합
https://www.acmicpc.net/problem/1735
'''

a, b = map(int, input().split())
c, d = map(int, input().split())

e = a*d + c*b
f = b*d

# 유클리드 알고리즘 사용
def gcd(m,n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

print((e // gcd(e, f)), f // gcd(e, f))
