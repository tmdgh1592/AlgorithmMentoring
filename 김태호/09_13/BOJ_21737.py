#-*- coding:utf-8 -*-
import sys
from operator import add, mul, sub, truediv
import re

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

input = sys.stdin.readline
n = int(input().rstrip())
arr = [int(x) if x.isdigit() else x for x in re.findall(r'[\D]|[\d]+', input().rstrip())]
div = lambda x, y: int(truediv(x, y))
operator = {'S' : sub, 'M' : mul, 'U' : div, 'P' : add}
res = arr[0]
ans = []

for sth in arr[1:]:
    if sth == 'C':
        ans.append(res)
    elif isinstance(sth, str):
        op = operator[sth]
    else:
        res = op(res, sth)

if ans:
    print(*ans)
else:
    print('NO OUTPUT')
