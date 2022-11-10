#-*- coding:utf-8 -*-
import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
graph = list(MIS())
q = deque([(0, 0)])
res = sys.maxsize
visited = [False] * n

while q:
    cnt, now = q.popleft()
    if now == n - 1:
        res = min(res, cnt)
        continue

    for jump in range(1, graph[now] + 1):
        if now + jump > n - 1: break
        if visited[now + jump]: continue
        visited[now + jump] = True
        q.append((cnt + 1, now + jump))

print(-1 if res == sys.maxsize else res)