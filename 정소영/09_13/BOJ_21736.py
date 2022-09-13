#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
sys.setrecursionlimit(10**7)

n, m = MIS()
data = [list(input().rstrip()) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

p = 0

def in_range(y, x):
    return (x >= 0 and x < m) and (y >= 0 and y < n)

visited = [[0 for _ in range(m)] for _ in range(n)]

def dfs(y, x):
    global p

    if data[y][x] == 'P': 
        p += 1
    
    visited[y][x] = 1
        
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]

        if not in_range(ny, nx): continue
        if visited[ny][nx]: continue
        if data[ny][nx] =='X': continue
        dfs(ny, nx)

start_X = -1
start_Y = -1

for i in range(n):
    for j in range(m):
        if data[i][j] == 'I':
            start_Y = i
            start_X = j

dfs(start_Y, start_X)

if p != 0:
    print(p)
else:
    print('TT')