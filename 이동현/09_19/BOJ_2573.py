import sys
from collections import defaultdict, deque
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())


n, m = MIS()
ice_location = deque()
melt_count = defaultdict(int)
artic = list()
year = 0

for _ in range(n):
    artic.append(list(MIS()))

for i in range(n):
    for j in range(m):
        if artic[i][j]:
            ice_location.append((i, j))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    return (y > 0 and y < n) and (x > 0 and x < m)

def bfs():
    while ice_location:
        cur_node = ice_location.pop()
        y, x = cur_node
        visited[y][x] = True
        melt_count[(y, x)] = 0

        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if in_range(ny, nx): continue
            if visited[ny][nx] == True: continue
            if artic[nx][ny] == 0:
                melt_count[(y, x)] += 1
            else:
                ice_location.append((ny,nx))
            ice_location.append((y,x))
    return 1
ice_cnt = 0
while ice_location and ice_cnt < 2:
    ice_cnt = 0
    visited = visited = [[False] * m for _ in range(n)]
    for i in range(len(ice_location)):
        ice_cnt += bfs()

    for ice in ice_location:
        artic[ice[0]][ice[1]] -= melt_count[(ice[0], ice[1])]
        if artic[ice[0]][ice[1]] < 0:
            artic[ice[0]][ice[1]] = 0
    print(ice_cnt)
    year += 1

print(year)