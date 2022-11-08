#-*- coding:utf-8 -*-
import heapq
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
graph = [list(MIS()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
q = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            visited[i][j] = True
            q.append((0, i, j))

body = 2
ate = res = 0

opers = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    distance, x, y = heapq.heappop(q)

    if 0 < graph[x][y] < body:
        ate += 1
        res += distance
        graph[x][y] = 0

        if ate == body:
            body += 1
            ate = 0

        q = []
        distance = 0
        visited = [[False] * n for _ in range(n)]
        visited[x][y] = True
    
    for oper in opers:
        nx, ny = x+oper[0], y+oper[1]
        if not (0 <= nx < n and 0 <= ny < n): continue
        if visited[nx][ny]: continue
        if graph[nx][ny] > body: continue
        visited[nx][ny] = True
        heapq.heappush(q, (distance + 1, nx, ny))

print(res)