'''
피보나치 수 5
https://www.acmicpc.net/problem/10870
'''

import sys

n = int(sys.stdin.readline())

def fibo(k):
    if k == 0:
        return 0
    elif k==1 or k==2:
        return 1
    else:
        return fibo(k-1) + fibo(k-2)

print(fibo(n))
