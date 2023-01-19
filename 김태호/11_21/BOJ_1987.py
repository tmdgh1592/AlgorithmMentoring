#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(1 << 16)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

r, c = MIS()
table = list()


for i in range(r):
    table.append(input().rstrip())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

res = 0
alpha = [0 for _ in range(26)]
alpha[ord(table[0][0]) - ord('A')] = 1

def in_range(y, x):
    return 0 <= y < r and 0 <= x < c

def dfs(y, x, cnt):
    global res
    if res < cnt: res = cnt

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]

        if not in_range(ny, nx): continue
        if alpha[ord(table[ny][nx])  - ord('A')] == 1: continue
        
        alpha[ord(table[ny][nx]) - ord('A')] = 1
        dfs(ny, nx, cnt + 1)
        alpha[ord(table[ny][nx]) - ord('A')] = 0

dfs(0, 0, 1)
print(res)