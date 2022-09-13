#-*- coding:utf-8 -*-
import sys
from collections import defaultdict
sys.setrecursionlimit(int(1e9))
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

graph = defaultdict(list)

n, s, p = MIS()
check = [True for _ in range(s + 1)] + [False for _ in range(n - s)]
dist = []

for _ in range(n - 1):
    u, v = MIS()
    graph[u].append(v)
    graph[v].append(u)

def dfs(here, cnt):
    if here == p:
        return cnt
    ret = 0
    check[here] = True
    for there in graph[here]:
        if check[there]:
            continue
        ret += dfs(there, cnt + 1)
    return ret


for i in range(1, s + 1):
    dist.append(dfs(i, 0))

dist.sort()
print(n - sum(dist[0:2]) - 1)


