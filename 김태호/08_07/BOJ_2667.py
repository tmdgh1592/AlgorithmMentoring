#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def in_range(y, x):
    return (y >= 0 and y < len(data)) and (x >= 0 and x < len(data))

def dfs(y, x):
    visited[y][x] = True
    ret = 1
    
    for dir in range(len(dy)):
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if not in_range(ny, nx): continue
        if visited[ny][nx]: continue
        if data[ny][nx] == '0': continue
        ret += dfs(ny, nx)
    
    return ret

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

data = [input().rstrip() for _ in range(int(input()))]
visited = [[False for _ in range(len(data))] for _ in range(len(data))]
res = list()

for i in range(len(data)):
    for j in range(len(data)):
        if visited[i][j]: continue
        if data[i][j] == '0': continue

        tmp = dfs(i, j)
        if not tmp: continue
        res.append(tmp)

print(len(res), *sorted(res), sep='\n')