'''
최소공배수
https://www.acmicpc.net/problem/13241
'''
# 유클리드 알고리즘
a, b = map(int, input().split())

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

result = (a * b) // gcd(a, b)

print(result)
