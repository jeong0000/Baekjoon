'''
문자열 집합
https://www.acmicpc.net/problem/14425
'''

n, m = map(int, input().split())

dic_s={}
for i in range(n):
    dic_s[input()] = 1

cnt = 0
for i in range(m):
    if input() in dic_s:
        cnt += 1

print(cnt)
