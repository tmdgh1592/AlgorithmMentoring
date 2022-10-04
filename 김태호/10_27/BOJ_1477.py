#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m, l = MIS()
data = [0] + sorted(MIS()) + [l]

lo, hi = 1, l - 1

while lo <= hi:
    cnt = 0
    mid = (lo + hi) // 2
    
    for i in range(1, len(data)):
        if data[i] - data[i - 1] > mid:
            cnt += (data[i] - data[i - 1] - 1) // mid
    if cnt > m:
        lo = mid + 1
    else:
        hi = mid - 1
        res = mid
print(res)