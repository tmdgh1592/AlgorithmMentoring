#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

dy = [2, 2, -1, 1, -2, -2, -1, 1]
dx = [-1, 1, 2, 2, -1, 1, -2, -2]

def in_range(y, x):
    global l
    return((y >= 0 and y < l) and (x >= 0 and x < l))

def bfs(cy, cx, my, mx):
    q = deque()
    q.append((cy, cx))
    visited[cy][cx] = 1

    while q:
        y, x = q.popleft()

        if y == my and x == mx:
            print(visited[y][x] - 1)
            break

        for dir in range(8):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if not in_range(ny,nx): continue
            if visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))

t = int(input())

for _ in range(t):
    l = int(input())
    visited = [[0 for _ in range(l)] for _ in range(l)]
    cur_y, cur_x = MIS()
    move_y, move_x = MIS()
    bfs(cur_y, cur_x, move_y, move_x)