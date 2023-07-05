'''
영단어 암기는 괴로워
https://www.acmicpc.net/problem/20920
'''

import sys

n, m = map(int, sys.stdin.readline().split())

word_list = {}
for _ in range(n):
    word = sys.stdin.readline().rstrip()

    if len(word) >= m:
        if word in word_list:
            word_list[word] += 1
        else:
            word_list[word] = 1

word_list = sorted(word_list.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for i in word_list:
    print(i[0])
