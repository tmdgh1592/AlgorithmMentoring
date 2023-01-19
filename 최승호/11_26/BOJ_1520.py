#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(int(1e7))

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def f(x, y):
    if x == r - 1 and y == c - 1:
        return 1
    if cache[x][y] != -1:
        return cache[x][y]
    
    cache[x][y] = 0
    for oper in opers:
        nx, ny = x + oper[0], y + oper[1]
        if not((0 <= nx < r) and (0 <= ny < c)): continue
        if data[x][y] <= data[nx][ny]: continue
        cache[x][y] += f(nx, ny)

    return cache[x][y]


r, c = MIS()
data = [list(MIS()) for _ in range(r)]
# cache[x][y] := x, y까지 이동한 경로의 개수
cache = [[-1] * c for _ in range(r)]
opers = [(-1, 0), (1, 0), (0, -1), (0, 1)]

print(f(0, 0))