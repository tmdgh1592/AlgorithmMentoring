import sys
sys.setrecursionlimit(1 <<  14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = [list(MIS()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
cnt = 0
result = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    global n
    return (y >= 0 and y < n) and (x >= 0 and x < n)

def dfs(y, x, h):
    global cnt
    visited[y][x] = True

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if not in_range(ny, nx): continue
        if not arr[ny][nx]: continue
        if visited[ny][nx]: continue
        if arr[ny][nx] <= h: continue
        
        dfs(ny, nx, h)
        

for h in range(1, 101):
    cnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] and not visited[i][j]:
                if arr[i][j] <= h: continue
                dfs(i, j, h)
                cnt += 1
    result.append(cnt)
print(max(result))