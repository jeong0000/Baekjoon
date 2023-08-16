'''
연산자 끼워넣기
https://www.acmicpc.net/problem/14888
'''

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_n = -1e9
min_n = 1e9

def btk(add, sub, mul, div, sum, i):
    global max_n, min_n

    if i == n:
        max_n = max(max_n, sum)
        min_n = min(min_n, sum)
        return
    
    if add:
        btk(add-1, sub, mul, div, sum + a[i], i+1)
    if sub:
        btk(add, sub-1, mul, div, sum - a[i], i+1)
    if mul:
        btk(add, sub, mul-1, div, sum * a[i], i+1)
    if div:
        btk(add, sub, mul, div-1, int(sum/a[i]), i+1)

btk(add, sub, mul, div, a[0], 1)
print(int(max_n))
print(int(min_n))

'''
# permutations 사용 - PyPy3로 제출

import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
op = "+" * add + "-" * sub + "*" * mul + "/" * div

max_n = -1e9
min_n = 1e9

def insert_op():
    global max_n, min_n

    for case in permutations(op, n-1):
        result = a[0]

        for i in range(1, n):
            if case[i-1] == "+":
                result += a[i]
            elif case[i-1] == "-":
                result -= a[i]
            elif case[i-1] == "*":
                result *= a[i]
            elif case[i-1] == "/":
                result = int(result/a[i])

        max_n = max(result, max_n)
        min_n = min(result, min_n)

insert_op()
print(max_n)
print(min_n)
'''
