'''
스도쿠
https://www.acmicpc.net/problem/2580
'''

#PyPy3로 제출

import sys
input = sys.stdin.readline

# x의 행에 n이 있는지 확인
def row(x, n):
    for i in range(9):
        if sudoku[x][i] == n:
            return False
    return True

# x의 열에 n이 있는지 확인
def col(y, n):
    for i in range(9):
        if sudoku[i][y] == n:
            return False
    return True

# (x, y)가 포함된 정사각형에 n이 있는지 확인
def square(x, y, n):
    x = x // 3 * 3
    y = y // 3 * 3

    for i in range(3):
        for j in range(3):
            if sudoku[x+i][y+j] == n:
                return False
    return True

def btk(n):
    # 스도쿠 빈칸 채우기 완료 시 실행
    if n == len(zero):
        for i in sudoku:
            print(*i)
        exit(0)

    # 빈 칸에 1~10 넣어보기
    for i in range(1, 10):
        x = zero[n][0] # 빈 칸의 x 좌표
        y = zero[n][1] # 빈 칸의 y 좌표

        if row(x, i) and col(y, i) and square(x, y, i):
            sudoku[x][y] = i
            btk(n+1)
            sudoku[x][y] = 0 # 정답이 없을 경우 초기화

sudoku = []
zero= []

for i in range(9):
    sudoku.append(list(map(int, input().split())))
    for j in range(9):
        # 빈 칸일경우 zero 리스트에 추가
        if sudoku[i][j] == 0:
            zero.append([i,j])

btk(0)
