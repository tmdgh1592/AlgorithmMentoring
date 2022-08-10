#-*- coding:utf-8 -*-
import sys
from collections import defaultdict, deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

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
q = deque()
q.append(0)
visited[0] = True

while q:
    cur_node = q.popleft()
    res.append(cur_node)
    for next_node in g[cur_node]:
        if visited[next_node]: continue
        q.append(next_node)
        visited[next_node] = True

print(1 if res == data else 0)