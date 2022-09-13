#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

r, c = MIS()
data = [input().rstrip() for _ in range(r)]
res = list()
for i in range(r):
    tmp = list()
    for j in range(c // 2):
        if data[i][j] != '.':
            tmp.append(data[i][j])
        else:
            tmp.append(data[i][c - j - 1])
    tmp += tmp[::-1]
    res.append(''.join(tmp))
print(*res, sep='\n')