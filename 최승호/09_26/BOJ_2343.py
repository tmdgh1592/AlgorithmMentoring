#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def possible(size):
    interval_size = 0
    count = 1

    for x in arr:
        interval_size += x
        if interval_size > size:
            interval_size = x
            count += 1
        if count > m:
            return False
    return count <= m

n, m = MIS()
arr = list(MIS())
lo, hi = max(arr), sum(arr)

while lo <= hi:
    mid = (lo + hi) // 2
    if possible(mid): hi = mid - 1
    else: lo = mid + 1

print(lo)