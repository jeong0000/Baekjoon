'''
괄호
https://www.acmicpc.net/problem/9012
'''

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a = sys.stdin.readline().rstrip()

    stack = []
    for i in a:
        if i == '(':
            stack.append(1)
        elif i == ')':
            if len(stack) == 0:
                stack.append(0)
                break
            else:
                stack.pop()

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
