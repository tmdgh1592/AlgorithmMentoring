#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(1 << 16)
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def calc(idx):
    try:
        if idx - 1 >= 0:
            ret = ret = info[idx + s - 1] - info[idx - 1]
        else:
            ret = info[idx + s - 1]
    except:
        ret = -float('inf')
    return ret

def f(idx, cnt):
    if cnt == 3:
        return 0
    if idx >= n:
        return -float('inf')
    if cache[idx][cnt] != -1:
        return cache[idx][cnt]
    cache[idx][cnt] = max(f(idx + 1, cnt), f(idx + s, cnt + 1) + calc(idx))
    return cache[idx][cnt]

n = int(input())
data = list(MIS())
s = int(input())
info = [0 for _ in range(n)]
info[0] = data[0]
cache = [[-1 for _ in range(3)] for _ in range(n)]
for i in range(1, n):
    info[i] = info[i - 1] + data[i]

print(f(0, 0))
