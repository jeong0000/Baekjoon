'''
대칭 차집합
https://www.acmicpc.net/submit/1269
'''

a, b = map(int, input().split())

#차집합 계산하기 위해 집합함수(set) 사용
arr_1 = set(list(map(int, input().split())))
arr_2 = set(list(map(int, input().split())))

dif = len(arr_1) - len(arr_1 - arr_2)
print(len(arr_1) + len(arr_2) - 2*dif)
