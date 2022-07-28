import sys
sys.setrecursionlimit(1 <<  14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    global n, m
    return (y >= 0 and y < n) and (x >= 0 and x < m)

def dfs(y, x, py, px, color):
    if visited[y][x]: 
        return True 
    visited[y][x] = True

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if not in_range(ny, nx): continue
        if ny == py and nx == px: continue
        if colors[ny][nx] != color: continue
        if dfs(ny, nx, y, x, colors[ny][nx]):
            return True

    return False

n, m = MIS()
colors = [input().rstrip() for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if visited[i][j]: continue
        if dfs(i, j, -1, -1, colors[i][j]):
            print('Yes')
            exit(0)

print("No")




