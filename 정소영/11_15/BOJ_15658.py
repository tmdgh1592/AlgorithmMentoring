#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
data = list(MIS())
oper = list(MIS())

def f(idx, res):
    if idx == n:
        return res, res

    ansMax, ansMin = -float('inf'), float('inf')

    for i in range(4):
        if oper[i]:
            oper[i] -= 1
            if i == 0:
                ret = f(idx + 1, res + data[idx])
            elif i == 1:
                ret = f(idx + 1, res - data[idx])
            elif i == 2:
                ret = f(idx + 1, res * data[idx])
            elif i == 3:
                ret = f(idx + 1, int(res / data[idx]))
            ansMax = max(ret[0], ansMax)
            ansMin = min(ret[1], ansMin)
            oper[i] += 1
    return ansMax, ansMin

f(1, data[0])
print(*f(1, data[0]),sep='\n')