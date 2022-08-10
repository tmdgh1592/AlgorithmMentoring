#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(int(1e6))
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def dfs(here):
    ret = 0

    if not visited[here]:
        visited[here] = True
        if data[here]:
            ret += dfs(data[here]) + 1
        
    else:
        print(-1)
        exit(0)
    
    return ret

n, m, p = MIS()
data = [0 for _ in range(m + 1)]
visited = [False for _ in range(m + 1)]

for _ in range(n):
    u, v = MIS()
    if not data[v]:
        data[v] = u

print(dfs(p))

