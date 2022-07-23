#-*- coding:utf-8 -*-
import sys
from collections import deque
from collections import defaultdict
sys.setrecursionlimit(1 << 14)
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def dfs(cur, prev):
    if cache[cur] == 1: return cur
    cache[cur] = 1
    
    for next in g[cur]:
        if next == prev: continue
        res = dfs(next, cur)
        if res >= 0:
            cache[cur] = 2
            return res if cur != res else -2
        
    return -1

n = int(input())
g = defaultdict(list)
cache = [0 for _ in range(n)]
dist = [0 for _ in range(n)]
q = deque()

for _ in range(n):
    u, v = MIS()
    
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

dfs(0, -1)

for i in range(n):
    if cache[i] == 2:
        q.append(i)
        dist[i] = 0
        
    else:
        dist[i] = -1
        
while q:
    cur_node = q.popleft()
    
    for next_node in g[cur_node]:
        if dist[next_node] == -1:
            dist[next_node] = dist[cur_node] + 1
            q.append(next_node)
            
print(*dist)