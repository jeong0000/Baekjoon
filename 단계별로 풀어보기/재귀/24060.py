'''
알고리즘 수업 - 병합 정렬 1
https://www.acmicpc.net/problem/24060
'''

import sys

# 오름차순으로 정렬
def merge_sort(a, p, r):
    if (p < r):
        q = (p + r) // 2 # q => p, r의 중간 지점
        merge_sort(a, p, q) # 전반부 정렬
        merge_sort(a, q+1, r) # 후반부 정렬
        merge(a, p, q, r) # 병합l

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(a, p, q, r):
    global cnt, ans
    i = p
    j = q+1
    
    tmp = []
    while (i <= q and j <= r): # 분할 정렬된 list의 합병
        if (a[i] <= a[j]):
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1

    while (i <= q): # 왼쪽 배열 부분이 남은 경우, 남아 있는 값들을 일괄 복사
        tmp.append(a[i])
        i += 1
    while (j <= r): # 오른쪽 배열 부분이 남은 경우, 남아 있는 값들을 일괄 복사
        tmp.append(a[j])
        j += 1

    i = p
    t = 0

    while (i <= r): # 결과를 A[p..r]에 저장
        a[i] = tmp[t]
        cnt += 1
        if cnt == k:
            ans = a[i]
            break
        i += 1
        t += 1
    

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

cnt, ans = 0, -1

merge_sort(a, 0, n-1)
print(ans)
