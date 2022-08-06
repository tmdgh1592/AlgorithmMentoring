import sys
sys.setrecursionlimit(1 << 14)

MIS = lambda: map(int, input())

n = int(input())
house = []
for _ in range(n):
    house.append(list(MIS()))
    
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt_res = []

def in_range(y, x):
    global n
    return (x >= 0 and x < n) and (y >= 0 and y < n)

def dfs(y, x):
    global cnt
    visited[y][x] = True

    for dir in range(4):
        nx  = x + dx[dir]
        ny = y + dy[dir]

        if not in_range(ny, nx): continue
        if visited[ny][nx]: continue
        if not house[ny][nx]: continue
        dfs(ny, nx)
        cnt += 1


res = 0
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if house[i][j] and not visited[i][j]:
            cnt = 1
            dfs(i, j)
            res += 1
            cnt_res.append(cnt)
print(res)
for i in range(res):
    print(cnt_res[i])