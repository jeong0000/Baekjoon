'''
약수
https://www.acmicpc.net/problem/1037
'''

n = int(input())
ary = list(map(int, input().split()))
ary.sort()

if len(ary) == 1:
    print(ary[0] ** 2)
else:
    print(ary[0] * ary[len(ary)-1])
