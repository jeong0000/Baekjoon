'''
다음 소수
https://www.acmicpc.net/problem/4134
'''

import math

t = int(input())

# 소수는 1과 자기자신을 제외한 약수가 존재하지 않는 경우를 말함
# 약수들은 대칭적으로 짝을 이루기 때문에 자기 자신의 제곱근(루트)까지만 확인하면 됨
# ex) 12 -> 1 * 12, 2 * 6, 3 * 4, 4 * 3, 6 * 2, 12 * 1
def primeNum(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(t):
    n = int(input())

  # 0과 1은 소수 X
    if(n == 1 or n == 0):
        n = 2
    while True:
        if primeNum(n) != False:
            print(n)
            break
        else:
            n += 1
