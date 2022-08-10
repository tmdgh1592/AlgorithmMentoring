#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(int(1e6))
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def in_range(y, x):
    return (y >= 0 and y < len(data)) and (x >= 0 and x < len(data))

def dfs(y, x):
    visited[y][x] = True
    
    for dir in range(len(dy)):
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if not in_range(ny, nx): continue
        if visited[ny][nx]: continue
        if data[ny][nx] < height: continue
        dfs(ny, nx)
    
    return 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

data = [list(MIS()) for _ in range(int(input()))]


global_min = min(map(min, data))
global_max = max(map(max, data))

res = 0

for height in range(global_min, global_max + 1):
    tmp = 0
    visited = [[False for _ in range(len(data))] for _ in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data)):
            if visited[i][j]: continue
            if data[i][j] < height: continue
            tmp += dfs(i, j)
    res = max(tmp, res)


print(res)