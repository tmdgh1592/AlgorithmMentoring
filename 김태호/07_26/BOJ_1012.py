#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(1 << 14)
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def in_range(y, x):
    global n, m
    return (y >= 0 and y < n) and (x >= 0 and x < m)


def dfs(y, x):
    visited[y][x] = True
    
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if not in_range(ny, nx): continue
        if not arr[ny][nx]: continue
        if visited[ny][nx]: continue
        dfs(ny, nx)
    


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(int(input())):
    m, n, k = MIS()
    res = 0
    arr = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        u, v = MIS()
        arr[v][u] = 1
        
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:
                dfs(i, j)
                res += 1
    print(res)
