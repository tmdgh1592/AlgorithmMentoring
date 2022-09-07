import sys
from collections import deque
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

case = int(input())

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    global w, h
    return (y >= 0 and y < h) and (x >= 0 and x < w)

def init():
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                q.append((i, j, 0))
                visited[i][j] = True
            if arr[i][j] == "*":
                fq.append((i, j))
                visited_fire[i][j] = True

def bfs():
    for _ in range(len(q)):
        y, x, t = q.popleft()
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
        if not in_range(ny, nx):
            return t + 1
        if visited[ny][nx]: continue
        if arr[ny][nx] == '.':
            arr[ny][nx] = "@"
            visited_fire[ny][nx] = True
            q.append((ny, nx, t + 1))
    return -1

def fbfs():
    for _ in range(len(fq)):
        y, x = fq.popleft()
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
        if not in_range(ny, nx): continue
        if visited_fire[ny][nx]: continue
        if arr[ny][nx] != '#':
            arr[ny][nx] = True
            fq.append((ny, nx))

for _ in range(case):
    w, h = MIS()
    arr = [list(input().rstrip()) for _ in range(h)]

    visited = [[False for _ in range(w)] for _ in range(h)]
    visited_fire = [[False for _ in range(w)] for _ in range(h)]
    q = deque()
    fq = deque()

    init()

    while q or fq:
        fbfs()
        print(arr)
        res = bfs()
        if res != -1:
            break

    if res != -1: print(res)
    else: print('IMPOSSIBLE')
    