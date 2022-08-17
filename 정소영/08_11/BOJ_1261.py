#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

m, n = MIS()
arr = [list(map(int, input().rstrip())) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

def in_range(y, x):
    return (y >= 0 and y < n) and (x >= 0 and x < m)

q = deque()

visited = [[-1 for _ in range(m)] for _ in range(n)]
visited[0][0] = 0
def bfs(y, x):
    q.append((y, x))
    
    while q:
        y, x = q.popleft()

        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if not in_range(ny, nx): continue
            if visited[ny][nx] == -1 :
                if arr[ny][nx] == 0:
                    q.appendleft((ny, nx))
                    visited[ny][nx] = visited[y][x]
                else:
                    q.append((ny,nx))
                    visited[ny][nx] = visited[y][x] + 1
            

bfs(0,0)
print(visited[n-1][m-1])