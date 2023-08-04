'''
N과 M (2)
https://www.acmicpc.net/problem/15650
'''

#백트래킹 입문 문제 2

import sys
input = sys.stdin.readline

def btk():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n+1):
        if i in s:
            continue
        if len(s) == 0 or i > s[len(s)-1]:
            s.append(i)
            btk()
            s.pop()

n, m = map(int, input().split())
s = []
btk()
