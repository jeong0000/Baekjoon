'''
인사성 밝은 곰곰이
https://www.acmicpc.net/problem/25192
'''

import sys

n = int(sys.stdin.readline())

dic = {}
cnt = 0
for _ in range(n):
    a = sys.stdin.readline()
  
    # readline은 개행문자 붙어서 옴
    if a == 'ENTER\n':
        dic = {}
    else:
        if a not in dic:
            dic[a] = 1
            cnt += 1

print(cnt)
