#-*- coding:utf-8 -*-
from itertools import combinations
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
graph = [[] for _ in range(n+1)]
friend_count = [0] * (n+1)
check = [[False] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = MIS()
    graph[a].append(b); friend_count[a] += 1
    graph[b].append(a); friend_count[b] += 1
    check[a][b] = True; check[b][a] = True

res = sys.maxsize
for a in range(1, n-1):
    for b in range(a+1, n):
        if not check[a][b]: continue
        for c in range(b+1, n+1):
            if not check[b][c] or not check[c][a]: continue
            res = min(res, friend_count[a] + friend_count[b] + friend_count[c] - 6)

print(-1 if res == sys.maxsize else res)