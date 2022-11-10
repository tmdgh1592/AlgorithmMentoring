#-*- coding:utf-8 -*-
import sys
from operator import truediv

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
data = list(MIS())
opers = list(MIS())
min_res, max_res = sys.maxsize, -sys.maxsize

def f(now, val, cnt):
    global min_res, max_res

    if cnt == n:
        min_res = min(min_res, val)
        max_res = max(max_res, val)
        return

    for i in range(now, n):
        for j in range(4):
            if opers[j] <= 0: continue
            opers[j] -= 1
            if j == 0: f(i+1, val + data[i], cnt + 1)
            elif j == 1: f(i+1, val - data[i], cnt + 1)
            elif j == 2: f(i+1, val * data[i], cnt + 1)
            elif j == 3: f(i+1, int(truediv(val, data[i])), cnt + 1)
            opers[j] += 1

f(1, data[0], 1)
print(max_res, min_res, sep='\n')