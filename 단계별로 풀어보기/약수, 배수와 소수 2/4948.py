'''
베르트랑 공준
https://www.acmicpc.net/problem/4948
'''

import math, sys

# 딕셔너리 사용 안 할 경우, 입력값에 대해 다시 처음부터 소수의 개수를 찾기 때문에 값이 커질수록 시간이 오래 걸림
dic = {}
while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    cnt = 0
    for i in range(n+1, 2*n+1):
        if i == 1:
            continue

        if str(i) in dic:
            if dic[str(i)] == 'True':
                cnt += 1
        else:
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    dic[str(i)] = 'False'
                    break
            else:
                dic[str(i)] = 'True'
                cnt += 1

    print(cnt)
