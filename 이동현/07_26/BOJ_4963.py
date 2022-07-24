import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

def in_range(y, x):
    global h, w
    return (x >= 0 and x < w) and (y >= 0 and y < h)

def dfs(y, x):
    visited[y][x] = True

    for dir in range(8):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not in_range(ny, nx): continue
        if visited[ny][nx] == True : continue
        if not arr[ny][nx]: continue
        dfs(ny, nx)

while True:
    try:
        w, h = MIS()
    except:
        exit()

    arr = [list(MIS()) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    res = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] and not visited[i][j]:
                dfs(i, j)
                res += 1
    if h != 0 : print(res)