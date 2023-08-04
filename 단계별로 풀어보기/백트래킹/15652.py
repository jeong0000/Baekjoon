'''
N과 M (4)
https://www.acmicpc.net/problem/15652
'''

# 백트래킹 입문 문제 4

import sys
input = sys.stdin.readline

def btk():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n+1):
        if len(s) == 0 or i >= s[len(s)-1]:
            s.append(i)
            btk()
            s.pop()

n, m = map(int, input().split())
s = []
btk()
