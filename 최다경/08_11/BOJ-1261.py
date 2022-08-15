import sys
from collections import deque
MIS = lambda: map(int, input())
n, m = map(int, input().rstrip().split())

arr = [list(MIS()) for _ in range(m)]
dist = [[-1 for _ in range(n)] for _ in range(m)]
q = deque(list())
q.append([0, 0])
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def in_range(y, x):
    global n, m
    return (y >= 0 and y < n) and (x >= 0 and x < m)

def bfs(q, arr):
    global n, m
    while q:
        y, x = q.popleft()
        step = arr[y][x]
        if y == n - 1 and x == m - 1:
            return arr[y][x]
        
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if not in_range(ny, nx): continue
            if arr[ny][nx] != 0: continue
            arr[ny][nx] = step + 1
            q.append([ny, nx])

    return -1
