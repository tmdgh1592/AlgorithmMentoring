import sys
from collections import deque
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
m, n = MIS()
tomato = []
for _ in range(n):
    tomato.append(list(MIS()))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def in_range(y, x):
    return (x >= 0 and x < m) and (y >= 0 and y < n)

q = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j))

while q:
    cur_node = q.popleft()
    y, x= cur_node
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if not in_range(ny, nx): continue
        if tomato[ny][nx] == 0:
            tomato[ny][nx] = tomato[y][x] + 1
            q.append((ny, nx)) 
max_day = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit()
        max_day = max(max_day, tomato[i][j])
print(tomato)
print(max_day - 1)