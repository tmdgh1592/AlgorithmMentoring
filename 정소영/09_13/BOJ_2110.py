#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, c = MIS()
x = sorted([int(input()) for _ in range(n)])

lo = 1
hi = x[-1] - x[0]

def is_possible(dist):
    cnt = c - 1
    prev = x[0]

    for i in range(1, n):
        if prev + dist <= x[i]:
            cnt -= 1
            prev = x[i]

            if cnt < 0:
                cnt = 0
    
    if not cnt:
        return True
    
    return False

while lo <= hi:
    mid = (lo + hi) // 2

    if is_possible(mid):
        lo = mid + 1
    else:
        hi = mid - 1

print(hi)