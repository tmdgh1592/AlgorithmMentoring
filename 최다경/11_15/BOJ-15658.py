import sys
from operator import add, mul, truediv, sub
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

div = lambda x, y: int(truediv(x, y))
operator = {0: add, 1: sub, 2: mul, 3: div}
n = int(input())
data = list(MIS())
opers = list(MIS())

def bf(idx, res):
    if idx == n:
        return res, res

    ma = -float('inf')
    mi = float('inf')
    for i in range(4):
        if opers[i]:
            opers[i] -= 1
            ret = bf(idx + 1, operator[i](res, data[idx]))
            ma = max(ret[0], ma)
            mi = min(ret[1], mi)
            opers[i] += 1
    return ma, mi
x, y = bf(1, data[0])
print(x)
print(y)



