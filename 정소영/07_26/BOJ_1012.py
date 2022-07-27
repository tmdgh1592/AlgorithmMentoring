#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

sys.setrecursionlimit(10**6)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y,x):
    global n,m
    return ((y >= 0 and y < n) and (x >= 0 and x < m))

def dfs(y,x) :
    visited[y][x] = True
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if not in_range(ny,nx): continue
        if not arr[ny][nx]: continue
        if visited[ny][nx]: continue
        dfs(ny,nx)

def bfs(node):
    q = deque()
    q.append(node)

    while q:
        cur_node = q.popleft()
        y, x = cur_node
        
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if not in_range(ny,nx): continue
            if not arr[ny][nx]: continue
            arr[ny][nx] = 0
            q.append([ny,nx])

for _ in range(int(input())):
    m,n,k = MIS()
    arr = [[0] * m  for _ in range(n)]
    visited = [[False] * m  for _ in range(n)]
    res = 0
    for _ in range(k):
        x, y = MIS()
        arr[y][x] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:
                #dfs(i,j)
                bfs([i,j])
                res += 1
    print(res)
