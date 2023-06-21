'''
숫자 카드 2 - hashmap 사용
https://www.acmicpc.net/submit/10816/62293917
'''

import sys

a = sys.stdin.readline()
N = sorted(map(int, sys.stdin.readline().split()))
b = sys.stdin.readline()
M = map(int, sys.stdin.readline().split())

hashmap = {}
for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))
