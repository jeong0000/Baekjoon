'''
이항 계수 1
https://www.acmicpc.net/problem/11050
'''

# 이항계수 : 주어진 크기 집합에서 원하는 개수만큼 순서없이 뽑는 조합의 가짓수 -> nCk
# nCk = n!/k!(n-k)!

n, k = map(int, input().split())

def Febo(a):
    result = 1
    for i in range(2, a+2):
        result *= i
    
    result /= (a+1)
    return result

print(int(Febo(n) / (Febo(k) * Febo(n-k))))
