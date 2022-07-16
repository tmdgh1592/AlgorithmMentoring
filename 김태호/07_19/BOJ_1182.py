#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
a = list(MIS())

res = 0

for i in range(1, (1 << n)):
    if m == sum(a[j] for j in range(n) if (i & (1 << j))):
        res += 1
        
print(res)
