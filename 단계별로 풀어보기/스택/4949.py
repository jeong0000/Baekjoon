'''
균형잡힌 세상
https://www.acmicpc.net/problem/4949
'''

import sys

while True:
    a = sys.stdin.readline().rstrip()

    if a == ".":
        break

    stack = []
    for i in a:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")" or i == "]":
            if len(stack) == 0:
                stack.append(0)
                break
            elif (i == ")" and stack[len(stack)-1] == "(") or (i == "]" and stack[len(stack)-1] == "["):
                stack.pop()
            else:
                stack.append(0)
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")
