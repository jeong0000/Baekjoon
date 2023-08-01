'''
하노이 탑 이동 순서
https://www.acmicpc.net/problem/11729
'''

import sys

def hanoi(n, start, btw, end):
    if n == 1:
        print(start, end)
        return
    
    hanoi(n-1, start, end, btw)
    print(start, end)
    hanoi(n-1, btw, start, end)


n = int(sys.stdin.readline())
sum = 2**n-1
print(sum)
hanoi(n, 1, 2, 3)


'''
start(1) | between(2) | end(3)

n = 1) 1 0 0 -> 0 0 1
n = 2) 12 0 0 -> 2 1 0 -> 0 1 2 -> 0 0 12
n = 3) 
(12를 한 묶음으로 생각) 
123 0 0 -> 3 12 0 -> 0 12 3 -> 0 0 123

=> 
1. start에서 (n-1)개의 원판이 between으로 이동
2. start의 n 원판이 end로 이동
3. between에 있는 (n-1)개의 원판이 end로 이동
'''
