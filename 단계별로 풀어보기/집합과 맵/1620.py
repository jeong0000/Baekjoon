'''
나는야 포켓몬 마스터 이다솜
https://www.acmicpc.net/submit/1620
'''

import sys

#input() 사용 시 시간 초과 발생
n, m = map(int, sys.stdin.readline().split())

dic = {}
for i in range(n):
    # readline()으로 입력받을 시 생기는 "\n" 문자를 제거하기 위해 .rstrip() 필요
    a = sys.stdin.readline().rstrip()
    dic[a] = i+1
    dic[i+1] = a

for i in range(m):
    poc = sys.stdin.readline().rstrip()
    if poc.isdigit():
        print(dic[int(poc)])
    else:
        print(dic[poc])
