#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(1 <<  14)
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def in_range(y, x):
    global w, h
    return (y >= 0 and y < h) and (x >= 0 and x < w)


def dfs(y, x):
    visited[y][x] = True
    
    for dir in range(8):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if not in_range(ny, nx): continue
        if not arr[ny][nx]: continue
        if visited[ny][nx]: continue
        dfs(ny, nx)
    


dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, 1, -1, 1, -1]

while (data := MIS()):
    w, h = data
    if not w and not h:
        break
    res = 0
    arr = [list(MIS()) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
        
    for i in range(h):
        for j in range(w):
            if arr[i][j] and not visited[i][j]:
                dfs(i, j)
                res += 1
    print(res)
