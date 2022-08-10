#-*- coding:utf-8 -*-
import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def in_range(y, x):
    return (y >= 0 and y < n) and (x >= 0 and x < m)


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

m, n = MIS()
data = [input().rstrip() for _ in range(n)]
dist = [[-1 for _ in range(m)] for _ in range(n)]
q = deque()

q.append((0, 0))
dist[0][0] = 0

while q:
    y, x = q.popleft()
    for dir in range(len(dy)):
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if not in_range(ny, nx): continue
        if dist[ny][nx] != -1: continue
        if data[ny][nx] == '0':
            dist[ny][nx] = dist[y][x]
            q.appendleft((ny, nx))
        else:
            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))

print(dist[n - 1][m - 1])