'''
다리 놓기
https://www.acmicpc.net/problem/1010
'''

t = int(input())

def fac(n):
    result = 1
    for i in range(2, n+2):
        result *= i
    
    return (result//(n+1))

for _ in range(t):
    n,m = map(int, input().split())

    result = int(fac(m) / (fac(n) * fac(m-n)))

    print(result)
