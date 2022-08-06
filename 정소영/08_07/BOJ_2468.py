#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

sys.setrecursionlimit(100000)
n = int(input())
arr = [ list(MIS()) for _ in range(n)]

max_num = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] > max_num:
            max_num = arr[i][j]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    global n
    return ((y >= 0 and y < n) and (x >= 0 and x < n))


def dfs(y, x, num):
    visited[y][x] = True

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]

        if not in_range(ny, nx): continue
        if visited[ny][nx]: continue
        if arr[ny][nx] > num:
            visited[ny][nx] = True
            dfs(ny, nx, num)

res = 0

for max in range(max_num):
    cnt = 0
    visited = [[False] * (n + 1) for _ in range(n + 1)]
    
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                if arr[y][x] > max:
                    dfs(y, x, max)
                    cnt += 1

    if res < cnt:
        res = cnt
print(res)