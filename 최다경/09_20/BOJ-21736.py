import sys
from collections import deque
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
q = deque()
cnt = 0

def in_range(y, x):
    global n, m
    return (y >= 0 and y < n) and (x >= 0 and x < m)

n, m = MIS()
arr = [list(input().rstrip()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
        for j in range(m):
            if arr[i][j] == 'I':
                q.append([i, j])
while q:
    y, x = q.popleft()
    visited[y][x] = True
    if arr[y][x] == "P":
            cnt += 1
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if not in_range(ny, nx): continue
        if arr[ny][nx] == "X": continue
        if visited[ny][nx]: continue
        visited[ny][nx] = True
        q.append([ny, nx])
       
if cnt == 0: 
    print('TT')
    exit(0)
print(cnt)
