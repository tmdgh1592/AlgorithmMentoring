import sys
from operator import add, mul, sub, truediv

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

div = lambda x, y: int(truediv(x, y))
operator = {1 : sub, 2 : mul, 3 : div, 0 : add}

def f(idx, res):
    if idx == n:
        print("asdas")
        print(res)
        print("fin")
        print(res, res)
        return res, res
        
    max_val = -float('inf')
    min_val = float('inf')

    for i in range(4):
        if oper[i]:
            oper[i] -= 1
            ret = f(idx + 1, operator[i](res, num[idx]))
            max_val = max(ret[0], max_val)
            min_val = min(ret[1], min_val)
            oper[i] += 1
    return max_val, min_val

n = int(input())
num = list(MIS())
oper = list(MIS())

f(1, num[0])
print(*f(1, num[0]), sep=' ')