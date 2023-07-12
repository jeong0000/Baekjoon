'''
프린터 큐
https://www.acmicpc.net/problem/1966
'''

import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))

    cnt = 0
    while queue:
        mx = max(queue)
        
        if queue[0] == mx:
            queue.popleft()
            if m == 0:
                cnt += 1
                print(cnt)
                break
            else:
                cnt += 1
                m -= 1
        else:
            queue.append(queue.popleft())
            if m == 0:
                m = len(queue) -1 
            else:
                m -= 1
            
