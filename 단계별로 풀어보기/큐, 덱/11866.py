'''
요세푸스 문제 0
https://www.acmicpc.net/problem/11866
'''

import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())

queue = deque()
for i in range(1, n+1):
    queue.append(i)

result = []
while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<", end='')
print(', '.join(map(str, result)), end='')
print(">")
