'''
골드바흐 파티션
https://www.acmicpc.net/problem/17103
'''

# pypy3 로 제출, python3는 시간초과 발생
import math, sys

t = int(sys.stdin.readline())

def primeNum(k):
    for i in range(2, int(math.sqrt(k) + 1)):
        if k % i == 0:
            return False
    else:
        return True

dic = {}
for _ in range(t):
    n = int(sys.stdin.readline())

    if n == 1:
        print(0)
        continue

    cnt = 0
    for i in range(2, n // 2 + 1):
        a = i
        b = n - i

        if a not in dic:
            dic[a] = primeNum(a)
        if b not in dic:
            dic[b] = primeNum(b)

        if dic[a] and dic[b]:
            cnt += 1

    print(cnt)
