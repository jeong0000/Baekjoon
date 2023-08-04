'''
N과 M (3)
https://www.acmicpc.net/problem/15651
'''

# 백트래킹 입문 문제 3

import sys
input = sys.stdin.readline

def btk():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n+1):
        s.append(i)
        btk()
        s.pop()

n, m = map(int, input().split())
s = []
btk()
