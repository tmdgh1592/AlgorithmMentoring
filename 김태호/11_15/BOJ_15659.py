#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def f(depth, exp):
    if depth == n:
        ret = eval(exp)
        return ret, ret
    
    max_val = -float('inf')
    min_val = float('inf')
    
    for i in range(4):
        if oper[i]:
            oper[i] -= 1
            res = f(depth + 1, exp + operator[i] + data[depth])
            max_val = max(res[0], max_val)
            min_val = min(res[1], min_val)
            oper[i] += 1
    return max_val, min_val

n = int(input())
data = input().rstrip().split()
oper = list(MIS())
operator = {0 : '+', 1 : '-', 2 : '*', 3 : '//'}
print(*f(1, data[0]), sep='\n')