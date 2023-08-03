'''
덱 2
https://www.acmicpc.net/problem/28279
'''

import sys
from collections import deque

queue = deque()

n = int(sys.stdin.readline())
for _ in range(n):
    cmd = list(map(int, sys.stdin.readline().split()))

    if cmd[0] == 1:
        queue.appendleft(cmd[1])
    elif cmd[0] == 2:
        queue.append(cmd[1])
    elif cmd[0] == 5:
        print(len(queue))
    elif cmd[0] == 6:
        if queue:
            print(0)
        else:
            print(1)
    elif queue:
        if cmd[0] == 3:
            print(queue.popleft())
        elif cmd[0] == 4:
            print(queue.pop())
        elif cmd[0] == 7:
            print(queue[0])
        elif cmd[0] == 8:
            print(queue[len(queue) - 1])
    else:
        print(-1)
