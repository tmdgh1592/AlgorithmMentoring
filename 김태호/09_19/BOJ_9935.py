#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

data = input().rstrip()
boom = [x for x in input().rstrip()]
res = []

for c in data:
    res.append(c)
    if len(res) < len(boom):
        continue
    if res[-1] == boom[-1]:
        if res[-len(boom):] == boom:
            del res[-len(boom):]

if not res:
    print('FRULA')
else:
    print(''.join(res))
