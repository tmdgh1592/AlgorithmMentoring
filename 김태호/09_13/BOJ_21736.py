#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(int(1e9))
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
campus = [[x for x in input().rstrip()] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
start_y, start_x = -1, -1
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            start_y, start_x = i, j
            break
def inRange(y, x):
    return (y >= 0 and y < n) and (x >= 0 and x < m)

def dfs(y, x):
    visited[y][x] = True
    ret = 0
    if campus[y][x] == 'P':
        ret += 1
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if inRange(ny, nx) and campus[ny][nx] != 'X' and not visited[ny][nx]:
            ret += dfs(ny, nx)
    return ret

res = dfs(start_y, start_x)
if res != 0:
    print(res)
else:
    print('TT')
    