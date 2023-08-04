'''
N과 M (1)
https://www.acmicpc.net/problem/15649
'''


'''

다른 풀이 - itertools의 permutations 함수 사용(파이썬만 가능)

import sys, itertools
input = sys.stdin.readline

n, m = map(int, input().split())
ary = [i for i in range(1, n+1)]

c = itertools.permutations(ary, m)

for i in c:
    for j in i:
        print(j, end=" ")
    print()

## combinations : 중복 가능
    
'''
