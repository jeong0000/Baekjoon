'''
별 찍기 - 10
https://www.acmicpc.net/problem/2447
'''

import sys

def star(len):
    if len == 1:
        return "*"
    
    sen = star(len//3)
    ary = []

    for i in sen:
        ary.append(i*3)
    for i in sen:
        ary.append(i + ' '*(len//3) + i)
    for i in sen:
        ary.append(i*3)
    
    return ary

n = int(sys.stdin.readline())
print('\n'.join(star(n)))
