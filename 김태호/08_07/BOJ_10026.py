#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(int(1e6))
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def in_range(y, x):
    return (y >= 0 and y < len(data)) and (x >= 0 and x < len(data))

def dfs_normal(y, x):
    visited[y][x] = True
    
    for dir in range(len(dy)):
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if not in_range(ny, nx): continue
        if visited[ny][nx]: continue
        if data[y][x] != data[ny][nx]: continue
        dfs_normal(ny, nx)
    return None

def dfs_abnormal(y, x):
    visited[y][x] = True
    
    for dir in range(len(dy)):
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if not in_range(ny, nx): continue
        if visited[ny][nx]: continue
        if data[y][x] == 'R' or data[y][x] == 'G':
            if data[ny][nx] == 'R' or data[ny][nx] == 'G':
                dfs_abnormal(ny, nx)
        else:
            if data[y][x] == data[ny][nx]:
                dfs_abnormal(ny, nx)
    return None


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

data = [input().rstrip() for _ in range(int(input()))]

visited = [[False for _ in range(len(data))] for _ in range(len(data))]
res = 0

for i in range(len(data)):
    for j in range(len(data)):
        if not visited[i][j]:
            dfs_normal(i, j)
            res += 1
            
print(res, end=' ')

visited = [[False for _ in range(len(data))] for _ in range(len(data))]
res = 0

for i in range(len(data)):
    for j in range(len(data)):
        if not visited[i][j]:
            dfs_abnormal(i, j)
            res += 1
            
print(res)