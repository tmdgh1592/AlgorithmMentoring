#-*- coding:utf-8 -*-
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
data = list(MIS())
opers = list(MIS())
min_res, max_res = sys.maxsize, -sys.maxsize

def f(now, val):
    global min_res, max_res, ret

    if sum(opers) == 0:
        min_res = min(min_res, val)
        max_res = max(max_res, val)
        return
    

    for i in range(now + 1, n):
        for j in range(4):
            if opers[j] <= 0: continue

            opers[j] -= 1
            if j == 0: f(i, val + data[i])
            elif j == 1: f(i, val - data[i])
            elif j == 2: f(i, val * data[i])
            elif j == 3: f(i, int(val.__truediv__(data[i])))
            opers[j] += 1

f(0, data[0])
print(max_res, min_res, sep='\n')