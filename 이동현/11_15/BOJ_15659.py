import sys
from operator import truediv

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

div = lambda x, y: int(truediv(x, y))

operator = {1 : '-', 2 : '*', 3 : '//', 0 : '+'}
n = int(input())
num = list(MIS())
oper = list(MIS())

max_val = -float('inf')
min_val = float('inf')

def f(idx, temp):
    global max_val, min_val
    if idx == n:
        temp1 = eval(temp)
        max_val = max(temp1, max_val)
        min_val = min(temp1, min_val)
        return None

    for i in range(4):
        if oper[i]:
            oper[i] -= 1
            f(idx + 1, temp + operator[i] + str(num[idx]))
            oper[i] += 1

f(1,str(num[0]))
print(max_val, min_val,sep="\n")