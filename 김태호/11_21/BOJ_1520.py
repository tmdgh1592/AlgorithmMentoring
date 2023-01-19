#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(1 << 16)
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def in_range(y, x):
    return 0 <= y < r and 0 <= x < c

def f(y, x):
    if y == r - 1 and x == c - 1:
        return 1
    if cache[y][x] != -1:
        return cache[y][x]
    
    cache[y][x] = 0

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if not in_range(ny, nx): continue
        if data[y][x] <= data[ny][nx]: continue
        cache[y][x] += f(ny, nx)
    
    return cache[y][x]


r, c = MIS()
data = [list(MIS()) for _ in range(r)]
cache = [[-1 for _ in range(c)] for _ in range(r)]
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
print(f(0, 0))