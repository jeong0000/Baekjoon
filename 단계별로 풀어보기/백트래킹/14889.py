'''
스타트와 링크
https://www.acmicpc.net/problem/14889
'''

import sys
input = sys.stdin.readline

n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))

# 방문 리스트
visited = [False for _ in range(n)]
min_n = 100

def btk(depth, idx):
    global min_n

    if depth == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += s[i][j]
                elif not visited[i] and not visited[j]:
                    link += s[i][j]
        min_n = min(min_n, abs(start - link))
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            btk(depth+1, i+1)
            visited[i] = False

btk(0,0)
print(min_n)
