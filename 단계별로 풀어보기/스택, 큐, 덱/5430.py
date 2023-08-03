'''
AC
https://www.acmicpc.net/problem/5430
'''

import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    queue = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    # 입력값(n)이 0일 경우 빈 배열로 초기화
    if n == 0:
        queue = []

    flag = 0
    for i in p:
        if i == "R":
            flag += 1
            
            # reverse() 사용 시 시간초과 발생
            # reverse()의 시간복잡도 : O(n)
            # for 문 안에서의 사용이기에 시간복잡도 -> O(n^2)
            
        elif i == "D":
            if queue:
                if flag % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                print("error")
                break
    else:
        if flag % 2 != 0:
            queue.reverse()
        print("[" + ",".join(queue) + "]")
