#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

q = deque()

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    return (y < n and y >= 0) and ( x < m and x >= 0)

def bfs(y, x, wall):

    q.append((y, x, wall))
    visited[0][0][0] = 1

    while q:
        y, x, wall = q.popleft()
        if y == n - 1 and x == m - 1:
            return visited[y][x][wall]
            
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if not in_range(ny, nx): continue
            if visited[ny][nx][wall]: continue 
            if arr[ny][nx] == 0:
                q.append((ny, nx, wall))
                visited[ny][nx][wall] = visited[y][x][wall] + 1
            if wall == 0 and arr[ny][nx] == 1:
                q.append((ny, nx, 1))
                visited[ny][nx][1] = visited[y][x][wall] + 1
    return -1

print(bfs(0, 0, 0))