#-*- coding:utf-8 -*-
from collections import defaultdict, deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
relations = defaultdict(list)
visited = [False for _ in range(n)]

for _ in range(m):
    u, v = MIS()
    relations[u].append(v)
    relations[v].append(u)

def dfs(idx, cnt):

    if cnt == 4:
        print(1)
        exit(0)

    for i in relations[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False


for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)
