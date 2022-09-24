#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
graph = [list(MIS()) for _ in range(n)]
white = blue = 0

def inc_cnt(x, y):
    global white, blue
    if graph[x][y]: blue += 1
    else: white += 1

def is_square(x, y, size):
    now = graph[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if now != graph[i][j]: return False
    return True

def dfs(x, y, size):
    global white, blue

    # 현재 사각형이 정사각형이거나 잘게 쪼개진 경우 카운트
    if is_square(x, y, size) or size == 1: inc_cnt(x, y); return

    # 체크할 간격 범위
    interval = nsize = size // 2

    dfs(x, y, nsize)
    dfs(x+interval, y, nsize)
    dfs(x, y+interval, nsize)
    dfs(x+interval, y+interval, nsize)


dfs(0, 0, n)
print(white, blue, sep='\n')