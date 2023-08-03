'''
덱
https://www.acmicpc.net/problem/10866
'''

import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()
for _ in range(n):
    order = list(map(str, sys.stdin.readline().split()))

    if order[0] == "push_front":
        queue.appendleft(order[1])
    elif order[0] == "push_back":
        queue.append(order[1])
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        if len(queue) != 0:
            print(0)
        else:
            print(1)
    elif len(queue) != 0:
        if order[0] == "pop_front":
            print(queue.popleft())
        elif order[0] == "pop_back":
            print(queue.pop())
        elif order[0] == "front":
            print(queue[0])
        elif order[0] == "back":
            print(queue[-1])
    else:
        print(-1)
