'''
도키도키 간식드리미
https://www.acmicpc.net/problem/12789
'''

import sys
from collections import deque

wait_queue = deque()

n = int(sys.stdin.readline())
queue = deque(list(map(int, sys.stdin.readline().split())))
flag = 1
cnt = 1

while cnt <= n:
    if (len(queue) != 0) and queue[0] == cnt:
        queue.popleft()
        cnt += 1
    elif (len(wait_queue) != 0) and (wait_queue[len(wait_queue)-1] == cnt):
        wait_queue.pop()
        cnt += 1
    elif (len(wait_queue) == 0) or (wait_queue[len(wait_queue)-1] > queue[0]) :
        wait_queue.append(queue.popleft())
    else:
        flag = 0
        break

if flag == 1:
    print("Nice")
else:
    print("Sad")
