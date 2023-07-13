'''
팩토리얼 2
https://www.acmicpc.net/problem/27433
'''

import sys

n = int(sys.stdin.readline())

def fac(k):
    if k == 1:
        return 1
    else:
        return k * fac(k-1)

# 0! = 1
print(fac(n+1) // (n + 1))
