#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
data = list(MIS())
lo, hi = max(data), sum(data)
res = float('inf')

while lo <= hi:
    cnt = 1
    time = 0
    mid = (lo + hi) // 2
    for i in range(n):
        if time + data[i] > mid:
            time = 0
            cnt += 1
        time += data[i]
        
    if cnt > m:
        lo = mid + 1
    else:
        res = min(mid, res)
        hi = mid - 1
print(res)