'''
최소공배수
https://www.acmicpc.net/problem/1934
'''

t = int(input())

# 유클리드 알고리즘
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
        
for i in range(t):
    a, b = map(int, input().split())
    if(a<b):
        a, b = b, a
    
    result = (a * b) // gcd(a, b)

    print(result)
