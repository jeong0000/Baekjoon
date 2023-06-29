'''
팩토리얼
https://www.acmicpc.net/problem/10872
'''

# 0! = 1
# (n-1)! = n! / n

n = int(input())

result = 1
for i in range(2, n+2):
    result *= i

print(result//(n+1))
