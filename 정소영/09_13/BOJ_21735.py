#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
arr = [0] + list(MIS())
size = 1
idx, size, time = 0, 1, 0

ans = -1
def func(idx, size, time):
    global ans

    if idx >= n or time == m:
        ans = max(size, ans)
        return ans
    if idx <= n - 1:
        func(idx + 1, size + arr[idx + 1], time + 1)
    if idx <= n - 2:
        func(idx + 2, (size / 2) + arr[idx + 2], time + 1)
    
func(idx,size,time)

print(int(ans))
