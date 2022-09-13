#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(int(1e6))
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def is_possible(dist):
    prev = data[0]
    cnt = c - 1
    
    for i in range(1, n):
        if prev + dist <= data[i]:
            prev = data[i]
            cnt -= 1
        if not cnt:
            return True
    return not cnt

n, c = MIS()
data = sorted([int(input()) for _ in range(n)])
hi = max(data) - min(data)
lo = 1

while lo <= hi:
    mid = (lo + hi) // 2
    
    if is_possible(mid):
        lo = mid + 1
    else:
        hi = mid - 1

print(hi)
