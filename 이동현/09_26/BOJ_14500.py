#진짜 모르겠다
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()

arr = list()
visited = [[False] * m for _ in range(n)]
for i in range(n):
    arr.append(list(MIS()))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

max_temp =  0

def in_range(y, x):
    return (0 <= y) and (y < n) and (0 <= x) and (x < m)

def dfs(y, x, cnt, res):
    global max_temp

    if cnt == 3:
        if max_temp < res: max_temp = res
    
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if not in_range(ny, nx): continue
        if visited[ny][nx]: continue
        visited[ny][nx] = True
        dfs(ny, nx, cnt + 1, res + arr[ny][nx])
        visited[ny][nx] = False
#구글링
def ou_shape(y, x):
    global max_temp
    if (y + 2) < m:
        temp = arr[y][x] + arr[y + 1][x] + arr[y + 2][x]
        if(x - 1) >= 0:
            max_temp = max(max_temp, temp + arr[y + 1][x - 1])
        if(x + 1) <= m:
            max_temp = max(max_temp, temp + arr[y + 1][x + 1])

    if (x + 2) < n:
        temp = arr[y][x] + arr[y][x + 1] + arr[y][x + 2]
        if(y - 1) >= 0:
            max_temp = max(max_temp, temp + arr[y - 1][x + 1])
        if(y + 1) <= n:
            max_temp = max(max_temp, temp + arr[y + 1][x + 1])

for y in range(n):
    for x in range(m):
        visited[y][x] = True
        dfs(y, x, 1, arr[y][x])
        visited[y][x] = False
        ou_shape(y, x)
print(max_temp)