'''
스택 수열
https://www.acmicpc.net/problem/1874
'''

import sys

n = int(sys.stdin.readline())
stack, result = [], []
c = 1

for _ in range(n):
    num = int(sys.stdin.readline())

    if len(stack) == 0 or stack[-1] < num:
        for i in range(c, num+1):
            stack.append(i)
            result.append("+")
            c += 1
        result.append("-")
        stack.pop()
    elif stack[-1] == num:
        result.append("-")
        stack.pop()
    elif stack[-1] > num:
        result.append("NO")
        break

if result[-1] == "NO":
    print("NO")
else:
    for i in result:
        print(i)
