#틀렸습니당
import sys
from collections import deque
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
ice = set()
entire_map = []
for _ in range(n):
    entire_map.append(list(MIS()))

for i in range(n):
    for j in range(m):
        if entire_map[i][j]:
            ice.add((i, j))


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    return (y > 0 and y < n) and (x > 0 and x < m)

def melt():
    global entire_map
    global ice
    # print(ice)
    remove_list = set()
    for i in ice:
        cnt = 0
        for dir in range(4):
            y = i[0] + dy[dir]
            x = i[1] + dx[dir]
            if not in_range(y, x): continue
            if entire_map[y][x] == 0:
                cnt += 1
        entire_map[i[0]][i[1]] -= cnt
        if entire_map[i[0]][i[1]] <= 0:
            entire_map[i[0]][i[1]] =0
            remove_list.add(i)
    ice = ice - remove_list
    # print(ice)

def dfs(y, x):
    visited[y][x] = True
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if not in_range(ny, nx): continue
        if visited[ny][nx] == True: continue
        if entire_map[ny][nx] == 0: continue
        dfs(ny, nx)
        return 1
    return 0

year = 0
ice_cnt = 0
cnt = 0
while ice_cnt < 2:
    visited = [[False for _ in range(m)] for _ in range(n)]
    # ice_cnt = 0
    year += 1
    cnt += 1
    melt()

    # print("남은 얼음",ice)
    for i in ice:
        ice_cnt += dfs(i[0],i[1])
        # print("year: ",year,"출력")
        # for j in visited:
        #     print(j)
        

# print("Asdsd")
# print(ice_cnt)
print(year)