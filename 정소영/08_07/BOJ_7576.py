#-*- coding:utf-8 -*-
from collections import deque
import sys

#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    global m, n
    return (y >= 0 and y < m) and (x >= 0 and x < n)

m, n = MIS()
tomato = [list(MIS()) for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]

        if not in_range(ny,nx): continue
        if tomato[nx][ny] == 0:
            tomato[nx][ny] = tomato[x][y] + 1
            q.append((nx, ny))

res = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res - 1)  