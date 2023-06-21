'''
듣보잡
https://www.acmicpc.net/submit/1764/62294526
'''

import sys

n, m = map(int, sys.stdin.readline().split())
non_hear, non_both = {}, {}

for i in range(n):
    non_hear[input()] = 1

for i in range(m):
    non_see = input()
    if non_see in non_hear:
        non_both[non_see] = 2
        
non_both = sorted(non_both)

print(len(non_both))
for i in non_both:
    print(i)
