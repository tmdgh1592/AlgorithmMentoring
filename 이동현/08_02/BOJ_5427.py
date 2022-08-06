import sys
from collections import deque
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

case_loop = int(input())

def in_range(y, x):
    return (x >= 0 and x < w) and (y >= 0 and y < h)

dy = [1, -1, 0 , 0]
dx = [0 , 0, 1, -1]

for _ in range(case_loop):
    w, h = MIS()
    building = []
    visited = [[0 for _ in range(w)] for _ in range(h)]
    q = deque()
    for i in range(h):
        building.append(list(input().rstrip()))

        if '@' in building[i]:
            q.append((i, building[i].index('@'), 0))

        if '*' in building[i]:
            for k in range(w):
                if building[i][k] == '*':
                    q.append((i, k, -1))

    while q:
        cur_node = q.popleft()
        y, x, t= cur_node

        if (building[y][x] != '*') and (t > -1) and (x == 0) or (y == 0) or (x == w -1) or (y == h -1):
            t += 1
            break

        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if not in_range(ny, nx): continue
            if building[ny][nx] == '#' : continue
            if t > -1 and building[ny][nx] == '.':
                building[ny][nx] = '@'
                q.append((ny, nx, t + 1))
            if t == -1 and building[ny][nx] != '*':
                building[ny][nx] = '*'
                q.append((ny, nx, -1))
    if t > 0:
        print(t)
    else:
        print('IMPOSSIBLE')
    
