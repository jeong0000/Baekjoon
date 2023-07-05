'''
제로
https://www.acmicpc.net/problem/10773
'''

import sys

k = int(sys.stdin.readline())

stack = []
for _ in range(k):
    n = int(sys.stdin.readline())
    
    if n == 0:
        if len(stack) != 0:
            del stack[len(stack)-1]
    else:
        stack.append(n)

print(sum(stack))
