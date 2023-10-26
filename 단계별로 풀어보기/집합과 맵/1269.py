'''
대칭 차집합
https://www.acmicpc.net/submit/1269
'''

a, b = map(int, input().split())

#차집합 계산하기 위해 집합함수(set) 사용
arr_1 = set(list(map(int, input().split())))
arr_2 = set(list(map(int, input().split())))

print(len(arr_1 ^ arr_2))

'''
교집합
print(arr_1 & arr_2)
print(arr_1.intersaction(arr_2))

합집합
print(arr_1 | arr_2)
print(arr_1.union(arr_2))

차집합
print(arr_1 - arr2)
print(arr_1.difference(arr_2))

대칭 차집합
print(arr_1 ^ arr_2)
'''
