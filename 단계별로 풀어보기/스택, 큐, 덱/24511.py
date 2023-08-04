'''
queuestack
https://www.acmicpc.net/problem/24511
'''


'''

첫번째 풀이 -> 시간초과
import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = deque(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))


for i in c:
    tmp = i
    for j in range(n):
        if a[j] == 0:
            switch = tmp
            tmp = b[j]
            b[j] = switch
    print(tmp, end=" ")
    
'''
