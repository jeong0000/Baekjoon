'''
숫자 카드 2 - 이진탐색 기반 풀이
https://www.acmicpc.net/problem/10816
'''

import sys

a = sys.stdin.readline()
N = sorted(map(int, sys.stdin.readline().split()))
b = sys.stdin.readline()
M = map(int, sys.stdin.readline().split())

def binary(n, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if n == N[m]:
        return N[start:end+1].count(n)
    elif n < N[m]:
        return binary(n, N, start, m-1)
    else:
        return binary(n, N, m+1, end)

n_dic = {}
for n in N:
    start = 0
    end = len(N) - 1
    if n not in n_dic:
        n_dic[n] = binary(n, N, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M ))
