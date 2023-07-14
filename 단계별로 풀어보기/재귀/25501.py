'''
재귀의 귀재
https://www.acmicpc.net/problem/25501
'''

import sys

t = int(sys.stdin.readline())

def recursion(s, l, r, cnt):
    cnt += 1
    if (l >= r): return 1, cnt
    elif (s[l] != s[r]): return 0, cnt
    else: return recursion(s, l+1, r-1, cnt)

def isPalindrome(s, cnt):
    return recursion(s, 0, len(s)-1, cnt)

for _ in range(t):
    s = sys.stdin.readline().rstrip()
    cnt = 0

    a, b = isPalindrome(s, cnt)
    print(a, b)
