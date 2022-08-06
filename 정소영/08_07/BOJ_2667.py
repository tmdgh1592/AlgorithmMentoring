#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

def in_range(y, x):
    global n
    return (y >= 0 and y < n) and (x >= 0 and x < n)

def bfs(y, x):
    q = deque()
    q.append((y, x))
    arr[y][x] = 0
    cnt = 1

    while q:
        y, x = q.popleft()

        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if not in_range(ny, nx): continue
            if not arr[ny][nx]: continue
            arr[ny][nx] = 0
            q.append((ny, nx))
            cnt += 1
    
    return cnt

n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

res = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            res.append(bfs(i,j))

res.sort()
print(len(res))
print(*res, sep='\n')
