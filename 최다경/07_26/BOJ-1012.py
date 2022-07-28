import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
result = []

def in_range(y, x):
    global n, m
    return(y >= 0 and y < n) and (x >= 0 and x < m)

def dfs(y, x):
    visited[y][x] = True

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not in_range(ny, nx): continue
        if not arr[ny][nx]: continue
        if visited[ny][nx]: continue
        dfs(ny, nx)

for _ in range(int(input())):
    m, n, k = MIS()
    arr = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    res = 0
    for i in range(k):
        u, v = MIS()
        arr[v][u] = 1

    for j in range(n):
        for l in range(m):
            if arr[j][l] and not visited[j][l]:
                dfs(j, l)
                res += 1
    result.append(res)

print(*result, sep='\n')



