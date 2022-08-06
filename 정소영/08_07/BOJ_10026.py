#-*- coding:utf-8 -*-
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

sys.setrecursionlimit(1 << 14)
n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[False] * n for _ in range(n)]

def in_range(y, x):
    return (y >= 0 and y < n) and (x >= 0 and x < n)

def dfs(y, x, color):
    if visited[y][x]: return True

    visited[y][x] = True

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if not in_range(ny, nx): continue;
        if arr[ny][nx] != color: continue;
        dfs(ny, nx, arr[ny][nx])

cnt = 0
for row in range(n):
    for col in range(n):
        if visited[row][col]: continue;
        dfs(row, col, arr[row][col])
        cnt += 1

rgw_cnt = 0

for row in range(n):
    for col in range(n):
        if arr[row][col] == 'R':
            arr[row][col] = 'G'

visited = [[False for _ in range(n)] for _ in range(n)]

for row in range(n):
    for col in range(n):
        if visited[row][col]: continue;
        dfs(row, col, arr[row][col])
        rgw_cnt += 1
        
print(cnt, rgw_cnt)