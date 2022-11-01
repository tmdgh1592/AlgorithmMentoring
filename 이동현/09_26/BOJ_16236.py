import sys
from collections import deque
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
sea = list()
q = deque()
size = 2  #baby shark's size

for i in range(n):
    temp = list(MIS())
    if 9 in temp: 
        baby_x = temp.index(9)
        baby_y = i
        temp[baby_x] = 0
    sea.append(temp)




dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x): 
    return (0 <= y) and (y < n) and (0 <= x) and (x < n)

def bfs(y, x, size):
    rst = []
    visited = [[0] * n for _ in range(n)]
    q.append((y, x))

    while q:
        cur_node = q.popleft()
        y, x = cur_node
        visited[y][x] = 1

        for i in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if not in_range[ny][nx]: continue
            if visited[ny][nx]: continue
            if sea[ny][nx] > size: continue
            q.append((ny, nx))
            visited[ny][nx] = visited[y][x] + 1
            if sea[ny][nx] > 0 and sea[ny][nx] < size:
                rst.append((ny, nx, visited[ny][nx]))
        rst = sorted(rst, key=lambda x: (x[2], -x[0], x[1]))
        return rst

time = 0

while True:
    s = bfs(baby_y, baby_x, size)
    if not s: break
    y, x, dist = s[0]
    time += (dist - 1)
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0