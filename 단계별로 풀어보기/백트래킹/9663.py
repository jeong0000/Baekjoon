'''
N-Queen
https://www.acmicpc.net/problem/9663
'''

#pypy3로 제출

import sys
input = sys.stdin.readline

n = int(input())

result = 0
row = [0] * n # 같은 행에 존재할 수 없으므로 한 행에 하나의 queen만 가능 -> 1차원 배열 사용 가능

def is_promising(x):
    for i in range(x):
        # row[x] == row[i] : 같은 열에 존재하는지 확인
        # abs(row[x] - row[i]) == abs(x - i) : 같은 대각선에 존재하는지 확인
        # 현재 위치 (2,1)일 경우, 오른쪽 대각선 (1,0), (3,2), (4,3) | 왼쪽 대각선 (0,3), (1,2), (3,0)
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def nQueen(x):
    global result
    if x == n:
        result += 1
        return
    
    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                nQueen(x+1)

nQueen(0)
print(result)
