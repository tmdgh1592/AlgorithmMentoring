#-*- coding:utf-8 -*-
import sys
from collections import defaultdict
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def dfs(here, cnt):
    if cnt == 4:
        print(1)
        exit()
    
    for there in g[here]:
        if not visited[there]:
            visited[there] = True
            dfs(there, cnt + 1)
            visited[there] = False

n, m = MIS()
g = defaultdict(list)
visited = [False for _ in range(n)]

for _ in range(m):
    u, v = MIS()
    g[u].append(v)
    g[v].append(u)


for here in range(n):
    visited[here] = True
    dfs(here, 0)
    visited[here] = False
    
print(0)
