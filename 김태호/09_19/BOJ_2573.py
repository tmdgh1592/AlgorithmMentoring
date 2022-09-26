#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(1 << 14)
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def in_range(y, x):
    return (y >= 0 and y < r) and (x >= 0 and x < c)

def go(y, x):
    visited[y][x] = True
    
    for dir in range(len(dy)):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if not in_range(ny, nx): continue
        if visited[ny][nx]: continue
        if not data[ny][nx]: continue
        go(ny, nx)

def check():
    res = 0
    for i in range(r):
        for j in range(c):
            if visited[i][j]: continue
            if not data[i][j]:continue
            go(i, j)
            res += 1
            if res >= 2: return True
    return res >= 2

def melt():
    how_many_water = [[0 for _ in range(c)] for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if not data[i][j]: continue
            for dir in range(len(dy)):
                ny = i + dy[dir]
                nx = j + dx[dir]
                if not in_range(ny, nx): continue
                if not data[ny][nx]: how_many_water[i][j] += 1
    
    for i in range(r):
        for j in range(c):
            if not how_many_water[i][j]: continue
            data[i][j] -= how_many_water[i][j]
            if data[i][j] < 0: data[i][j] = 0

r, c = MIS()
data = [list(MIS()) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
res = 0
while sum(map(sum, data)):
    melt()
    res += 1
    if check():
        print(res)
        exit(0)
    visited = [[False for _ in range(c)] for _ in range(r)]
print(0)