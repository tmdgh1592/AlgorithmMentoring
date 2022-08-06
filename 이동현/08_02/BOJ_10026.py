import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
color = []
for _ in range(n):
    color.append(input())
visited = [[False for _ in range(n)] for _ in range(n)]
blind_visited = [[False for _ in range(n)] for _ in range(n)]


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    global n
    return (x >= 0 and x < n) and (y >= 0 and y < n)

def dfs(y, x):
    visited[y][x] = True

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not in_range(ny, nx): continue
        if visited[ny][nx]: continue
        if color[ny][nx] != color[y][x]: continue
        dfs(ny, nx)

def blind_dfs(y, x):
    blind_visited[y][x] = True

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not in_range(ny, nx): continue
        if blind_visited[ny][nx]: continue
        if (color[ny][nx] == 'R' and color[y][x] == 'B') or (color[ny][nx] == 'G' and color[y][x] == 'B') or (color[ny][nx] == 'B' and color[y][x] == 'R') or (color[ny][nx] == 'B' and color[y][x] == 'G'): continue
        blind_dfs(ny, nx)

res = 0
blind_res = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            res += 1
        if not blind_visited[i][j]:
            blind_dfs(i, j)
            blind_res += 1
print(res, blind_res)