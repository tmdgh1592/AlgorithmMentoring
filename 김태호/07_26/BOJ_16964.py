#-*- coding:utf-8 -*-
import sys
from collections import defaultdict
sys.setrecursionlimit(int(1e6))
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def dfs(here):
    if visited[here]: return
    res.append(here)
    visited[here] = True
    for there in g[here]:
        dfs(there)
    return

n = int(input())
g = defaultdict(list)

for _ in range(n - 1):
    u, v = map(lambda x: x - 1, MIS())
    g[u].append(v)
    g[v].append(u)
data = list(map(lambda x: x - 1, MIS()))
order = [0 for _ in range(n)]

for i in range(n):
    order[data[i]] = i
    
for i in range(n):
    g[i] = sorted(g[i], key=lambda x: order[x])
    
res = list()
visited = [False for _ in range(n)]
dfs(0)

print(1 if res == data else 0)