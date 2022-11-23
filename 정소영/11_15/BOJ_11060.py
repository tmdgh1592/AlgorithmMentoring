#-*- coding:utf-8 -*-
import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = list(MIS())
visited = [False for _ in range(n)]

q = deque()

q.append((0,0))

while q:
    idx, res = q.popleft()

    if idx == n - 1:
        print(res)
        exit(0)

    for i in range(1, arr[idx] + 1):
        if i + idx > n - 1: break
        if visited[i + idx]: continue
        visited[i + idx] = True
        q.append((i + idx, res + 1))

print(-1)