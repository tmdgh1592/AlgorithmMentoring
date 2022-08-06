import sys
sys.setrecursionlimit(1 <<  14)
n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
cnt_h = 0
def in_range(y, x):
    global n
    return (y >= 0 and y < n) and (x >= 0 and x < n)

def dfs(y, x, color):
    global cnt
    visited[y][x] = True

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if not in_range(ny, nx): continue
        if visited[ny][nx]: continue
        if arr[ny][nx] != color: continue
        #cnt = 0
        dfs(ny, nx, arr[ny][nx])

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, arr[i][j])
            cnt += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, arr[i][j])
            cnt_h += 1
print(cnt, cnt_h)
            
