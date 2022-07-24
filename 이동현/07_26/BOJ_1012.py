import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    global n, m
    return (x >= 0 and x < m) and (y >= 0 and y < n)

def dfs(y, x):
    visited[y][x] = True
    
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if not in_range(ny, nx): continue
        if visited[ny][nx]: continue
        if not arr[ny][nx]: continue
        dfs(ny, nx)


for i in range(int(input())):
    m, n, k = MIS()
    res = 0 
    arr = [[False for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    for _ in range(k):
        a, b = MIS()
        arr[b][a] = True
    
    for i in range(n):
        for j in range(m):
            if arr[i][j]and not visited[i][j]:
                dfs(i, j)
                res += 1
    print(res)
