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
data = [list(MIS()) for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            q.append((i, j))


while q:
    y, x = q.popleft()
    for dir in range(len(dy)):
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if not in_range(ny, nx): continue
        if data[ny][nx] != 0: continue
        data[ny][nx] = data[y][x] + 1
        q.append((ny, nx))
        
res = -1

for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            print(-1)
            exit(0)
        res = max(res, data[i][j])
print(res - 1)