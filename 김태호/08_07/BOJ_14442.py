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

n, m, k = MIS()
data = [input().rstrip() for _ in range(n)]
dist = [[[0 for _ in range(11)] for _ in range(m)] for _ in range(n)]
q = deque()
q.append((0, 0, k))
dist[0][0][k] = 1

while q:
    y, x, remaining = q.popleft()
    
    if (y, x) == (n - 1, m - 1):
        print(dist[y][x][remaining])
        exit(0)
    
    for dir in range(len(dy)):
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if not in_range(ny, nx): continue
        if data[ny][nx] == '1' and remaining and not dist[ny][nx][remaining - 1]:
            dist[ny][nx][remaining - 1] = dist[y][x][remaining] + 1
            q.append((ny, nx, remaining - 1))
        elif data[ny][nx] == '0' and not dist[ny][nx][remaining]:
            dist[ny][nx][remaining] = dist[y][x][remaining] + 1
            q.append((ny, nx, remaining))
print(-1)