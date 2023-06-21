'''
숫자 카드
https://www.acmicpc.net/problem/10815
'''

n = int(input())
int_num = list(map(int, input().split()))
m = int(input())
num_m  = list(map(int, input().split()))

#딕셔너리 사용
dic = {}
for i in int_num:
    dic[i] = 1

for i in num_m:
    if i in dic:
        print(1, end=' ')
    else:
        print(0, end=' ')
        
'''
# 리스트로 할 경우 시간초과 발생

n = int(input())
int_num = list(map(int, input().split()))
m = int(input())
num_m  = list(map(int, input().split()))

for i in range(m):
    if(num_m[i] in int_num):
        print(1, end=' ')
    else:
        print(0, end=' ')
 '''
