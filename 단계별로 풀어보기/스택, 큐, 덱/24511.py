'''
queuestack
https://www.acmicpc.net/problem/24511
'''

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = int(input())
c = list(map(int, input().split()))

queue = deque()
for i in range(n):
    # 스택인 경우에는 입력, 출력값이 같아 변화 X => 큐인 경우만 실행
    # c[i]값이 들어오면 b[i] 값 출력
    if a[i] == 0:
        queue.appendleft(b[i])

# a가 다 스택(1)일 경우
else:
    if len(queue) == 0:
        # c 리스트 그대로 출력
        print(*c)
        # 코드 즉시 종료
        sys.exit()

for i in range(m):
    queue.append(c[i])
    print(queue.popleft(), end=" ")

'''

첫번째 풀이 -> 시간초과

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = deque(list(map(int, input().split())))

m = int(input())
c = list(map(int, input().split()))

for i in c:
    tmp = i
    for j in range(n):
        if a[j] == 0:
            switch = tmp
            tmp = b[j]
            b[j] = switch
    print(tmp, end=" ")
    
'''
