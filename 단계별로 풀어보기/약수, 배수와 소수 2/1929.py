'''
소수 구하기
https://www.acmicpc.net/problem/1929
'''

import math

m, n = map(int, input().split())

# 소수는 1과 자기자신을 제외한 약수가 존재하지 않는 경우를 말함
# 약수들은 대칭적으로 짝을 이루기 때문에 자기 자신의 제곱근(루트)까지만 확인하면 됨
# ex) 12 -> 1 * 12, 2 * 6, 3 * 4, 4 * 3, 6 * 2, 12 * 1
def primeNum(k):
    for i in range(2, int(math.sqrt(k)) + 1):
        if k % i == 0:
            return False
    return True

if(m == 1):
    m = 2

for i in range(m, n+1):  
    if primeNum(i) == True:
        print(i)
