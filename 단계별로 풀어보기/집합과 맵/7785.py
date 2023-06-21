'''
회사에 있는 사람
https://www.acmicpc.net/submit/7785/62285550
'''

n = int(input())

dic = {}
for i in range(n):
    name, statue = input().split()
    if name in dic:
        if statue == 'leave':
            del dic[name]
    else:
        dic[name] = statue

dic2 = sorted(dic, reverse=True)
for i in dic2:
    print(i)
