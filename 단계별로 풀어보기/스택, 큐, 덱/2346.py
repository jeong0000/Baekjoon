'''
풍선 터뜨리기
https://www.acmicpc.net/problem/2346
'''

import sys
from collections import deque

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
queue = deque(i+1 for i in range(n))

target = 1
for _ in range(n):
    print(queue.popleft(), end=" ")

    if queue:
        if p[target-1] > 0:
            for _ in range(p[target-1] - 1):
              # 오른쪽으로 rotation
              queue.append(queue.popleft())
            
        else:
            for _ in range(-p[target-1]):
              # 왼쪽으로 rotation
              queue.appendleft(queue.pop())

        target = queue[0]
