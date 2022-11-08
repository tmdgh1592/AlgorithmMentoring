#-*- coding:utf-8 -*-
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
data = list(MIS())
opers = list(MIS())
min_res, max_res = sys.maxsize, -sys.maxsize

def f(now, expr: str):
    global min_res, max_res

    if sum(opers) == 0:
        min_res = min(min_res, eval(expr))
        max_res = max(max_res, eval(expr))
        return
    

    for i in range(now + 1, n):
        for j in range(4):
            if opers[j] <= 0: continue

            opers[j] -= 1
            if j == 0: f(i, expr + "+" + str(data[i]))
            elif j == 1: f(i, expr + "-" + str(data[i]))
            elif j == 2: f(i, expr + "*" + str(data[i]))
            elif j == 3: f(i, expr + "//" + str(data[i]))
            opers[j] += 1

f(0, str(data[0]))
print(max_res, min_res, sep='\n')