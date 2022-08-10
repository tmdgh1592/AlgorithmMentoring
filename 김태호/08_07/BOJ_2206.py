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

n, m = MIS()
data = [input().rstrip() for _ in range(n)]
dist = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 1

while q:
    y, x, is_break = q.popleft()
    
    if (y, x) == (n - 1, m - 1):
        print(dist[y][x][is_break])
        exit(0)
    
    for dir in range(len(dy)):
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if not in_range(ny, nx): continue
        if data[ny][nx] == '1' and not is_break:
            dist[ny][nx][is_break ^ 1] = dist[y][x][is_break] + 1
            q.append((ny, nx, is_break ^ 1))
        elif data[ny][nx] == '0' and not dist[ny][nx][is_break]:
            dist[ny][nx][is_break] = dist[y][x][is_break] + 1
            q.append((ny, nx, is_break))
print(-1)