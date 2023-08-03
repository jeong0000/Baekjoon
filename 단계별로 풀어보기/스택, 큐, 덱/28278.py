'''
스택 2
https://www.acmicpc.net/problem/28278
'''

import sys
from collections import deque

queue = deque()

n = int(sys.stdin.readline())
for _ in range(n):
    cmd = list(map(int, sys.stdin.readline().split()))

    if cmd[0] == 1:
        queue.append(cmd[1])
    elif cmd[0] == 2:
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif cmd[0] == 3:
        print(len(queue))
    elif cmd[0] == 4:
        if queue:
            print(0)
        else:
            print(1)
    elif cmd[0] == 5:
        if queue:
            print(queue[len(queue)-1])
        else:
            print(-1)
