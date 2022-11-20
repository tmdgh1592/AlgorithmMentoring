#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(int(1e7))

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
data = [list(MIS()) for _ in range(n)]
cache = [[-1] * m for _ in range(n)]
opers = [(1, 0), (0, 1), (1, 1)]

def f(x, y):
    if x == n - 1 and y == m - 1:
        return data[x][y]
    if cache[x][y] != -1:
        return cache[x][y]
    
    for oper in opers:
        nx = x + oper[0]
        ny = y + oper[1]
        
        if 0 <= nx < n and 0 <= ny < m:
            cache[x][y] = max(cache[x][y], f(nx, ny) + data[x][y])
    
    return cache[x][y]
    
print(f(0, 0))