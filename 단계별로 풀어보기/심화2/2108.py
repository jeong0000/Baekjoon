'''
통계학
https://www.acmicpc.net/problem/2108
'''

import sys

n = int(sys.stdin.readline())

ary = []
for _ in range(n):
    a = int(sys.stdin.readline())
    ary.append(a)

# 산술평균
# round : 반올림 => ex) n = 0.466 / round(n,2) -> 0.47 / round(n) -> 0
print(round(sum(ary)/n))

# 중앙값
ary.sort()
print(ary[n//2])

# 최빈값
dic = {}
# 빈도수 세기
for i in ary:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

mx = max(dic.values())
mx_list = []
for i in dic:
    if dic[i] == mx:
        mx_list.append(i)

if len(mx_list) == 1:
    print(mx_list[0])
else:
    mx_list.sort()
    print(mx_list[1]) # 최빈값이 여러개일 경우 그 중 두번째로 작은 값 출력

# 최댓값과 최솟값 차이
print(max(ary) - min(ary))
