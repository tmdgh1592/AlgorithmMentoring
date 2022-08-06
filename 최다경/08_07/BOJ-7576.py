import queue
import sys
from collections import deque
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

m, n = MIS()
arr = [list(MIS()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

q = deque(list())

def in_range(y, x):
    global n, m
    return (y >= 0 and y < n) and (x >= 0 and x < m)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i, j])

while q:
    tmp = q.popleft()
    y, x = tmp
    day = arr[y][x] 

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]

        if not in_range(ny, nx): continue
        if arr[ny][nx] != 0: continue
        arr[ny][nx] = day + 1
        q.append([ny, nx])
ma = max(map(max, arr))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(-1)
            exit(0)

print(ma - 1)


    