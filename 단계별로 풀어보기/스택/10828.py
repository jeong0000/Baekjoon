'''
스택
https://www.acmicpc.net/problem/10828
'''

import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    order= list(map(str, sys.stdin.readline().split()))

    if(order[0] == 'push'):
        stack.append(order[1])
    elif(order[0] == 'pop'):
        if len(stack) != 0:
            print(stack[len(stack)-1])
            stack.pop()
        else:
            print(-1)
    elif(order[0] == 'size'):
        print(len(stack))
    elif(order[0] == 'empty'):
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif(order[0] == 'top'):
        if len(stack) != 0:
            print(stack[len(stack)-1])
        else:
            print(-1)
