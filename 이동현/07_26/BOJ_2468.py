import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
h = list()
for _ in range(n):
    h.append(list(MIS()))

MAX = max(map(max, h))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[0 for _ in range(n)] for _ in range(n)]
res = 0
res_list = list() #안전영역의 갯수를 담을 배열

def init():
    global visited, res
    res = 0 
    visited = [[0 for _ in range(n)] for _ in range(n)]

def in_range(y, x):
    global n
    return (x >= 0 and x < n) and (y >= 0 and y < n)

def dfs(y, x, height):
    visited[y][x] = True
    
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if visited[y][x]: continue
        if not in_range(ny, nx): continue
        if not h[nx][ny] > height : continue 
        
        dfs(ny, nx, height)

for height in range(MAX):
    init()
    for i in range(n):
        for j in range(n):
            if h[j][i] > height and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j, height)
                res += 1
    res_list.append(res)

print(max(res_list))
