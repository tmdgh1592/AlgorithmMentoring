#-*- coding:utf-8 -*-
import sys

#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def in_range(y, x):
    return (y >= 0 and y < n) and (x >= 0 and x < m)

def dfs(y, x, py, px, color):
    if visited[y][x]: return True

    visited[y][x] = True

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if not in_range(ny, nx): continue;
        if ny == py and nx == px: continue;
        if data[ny][nx] != color: continue;
        if dfs(ny, nx, y, x, data[ny][nx]):
            return True
    
    return False
    

n, m = MIS()
data = [input().rstrip() for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for row in range(n):
    for col in range(m):
        if visited[row][col]: continue;
        if dfs(row, col, -1, -1, data[row][col]):
            print('Yes')
            exit(0)
            
print('No')
            