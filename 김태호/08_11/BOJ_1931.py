#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
data = sorted([list(MIS()) for _ in range(n)], key=lambda x: (x[-1], x[0]))
res = 0
prev_end_time = -1

for start, end in data:
    if prev_end_time <= start:
        res += 1
        prev_end_time = end
print(res)