'''
칸토어 집합
https://www.acmicpc.net/problem/4779
'''

import sys

def kan(s,n):
    if n == 1:
        return
    for i in range(s + n//3, s +(n//3)*2):
        line[i] = " "
    kan(s, n//3)
    kan(s + n//3 * 2, n//3)

while True:
    try :
        n = int(sys.stdin.readline())
        line = ["-"]*(3**n)
		
        kan(0,3**n)
        print("".join(line))
    except : 
        break 
