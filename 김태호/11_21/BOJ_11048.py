#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(int(1e9))
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def in_range(y, x):
    return 0 <= y < n and 0 <= x < m

def f(y, x):
    if y == n - 1 and x == m - 1:
        return data[y][x]
    
    if cache[y][x] != -1:
        return cache[y][x]
    for dir in range(3):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if not in_range(ny, nx): continue
        cache[y][x] = max(f(ny, nx) + data[y][x], cache[y][x])
    return cache[y][x]

n, m = MIS()
data = [list(MIS()) for _ in range(n)]
cache = [[-1 for _ in range(m)] for _ in range(n)]
dy = [1, 0, 1]
dx = [0, 1, 1]
print(f(0, 0))