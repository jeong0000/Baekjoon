'''
가로수
https://www.acmicpc.net/problem/2485
'''

# 유클리드 알고리즘
def gcd(m,n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

n = int(input())

loc, loc_sub = [], []
for i in range(n):
    loc.append(int(input()))
    if(i > 0):
        loc_sub.append(loc[i] - loc[i-1]) # 입력으로 받은 값들의 간격 리스트

loc_sub2 = list(set(loc_sub)) # 간격 중복 제거

# loc_sub 값들의 최대공약수 구하기
m = loc_sub2[0]
for i in range(1, len(loc_sub2)):
    m = gcd(m, loc_sub2[i])

cnt = 0
for i in loc_sub:
    cnt += i // m - 1

print(cnt)
