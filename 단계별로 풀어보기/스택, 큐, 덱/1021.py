'''
회전하는 큐
https://www.acmicpc.net/problem/1021
'''

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
queue = deque(i+1 for i in range(n))

ary = list(map(int, sys.stdin.readline().split()))

cnt = 0
while ary:
    if ary[0] == queue[0]:
        queue.popleft()
        del ary[0]
    else:
        cnt += 1
        if queue.index(ary[0]) > len(queue) // 2:
            queue.appendleft(queue.pop())
        else:
            queue.append(queue.popleft())

print(cnt)
