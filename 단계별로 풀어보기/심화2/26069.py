'''
붙임성 좋은 총총이
https://www.acmicpc.net/problem/26069
'''

n = int(input())

cnt = 1
dic = {'ChongChong':1}

for _ in range(n):
    a, b = map(str, input().split())

    if(a in dic):
        if(b not in dic):
            dic[b] = 1
            cnt += 1
    elif(b in dic):
        if(a not in dic):
            dic[a] = 1
            cnt += 1
    
print(cnt)
