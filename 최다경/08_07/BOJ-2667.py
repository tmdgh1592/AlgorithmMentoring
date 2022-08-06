import sys
sys.setrecursionlimit(1 <<  14)

MIS = lambda: map(int, input())

n = int(input())
arr = [list(MIS()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
cnt = 0
apt = 1
result = []
apt_arr = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    global n
    return (y >= 0 and y < n) and (x >= 0 and x < n)

def dfs(y, x):
    global cnt, apt
    visited[y][x] = True

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        print(ny, nx)
        if not in_range(ny, nx): continue
        if not arr[ny][nx]: continue
        if visited[ny][nx]: continue
        apt += 1
        dfs(ny, nx)
        

for i in range(n):
    for j in range(n):
        if arr[i][j] and not visited[i][j]:
            dfs(i, j)
            cnt += 1
            apt_arr.append(apt)
            apt = 1
result.append(cnt)

print(*result)
print(*apt_arr, sep='\n')



        
