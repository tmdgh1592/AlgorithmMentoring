#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m, l = MIS()
arr = [0]+sorted(list(MIS()))+[l]
lo, hi = 1, l-1 # 1 ≤ 휴게소의 위치 ≤ L-1

def possible(mid):
    count = 0
    for i in range(1, n + 2):
        count += (arr[i] - arr[i-1] - 1) // mid
    return count > m

# mid : 설치할 휴게소 간격
while lo <= hi:
    mid = (lo + hi) // 2
    if possible(mid): lo = mid + 1
    else: hi = mid - 1

print(lo)