#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def reverse(sx, sy):
    for i in range(3):
        graph[sx+i][sy:sy+3] = list(map(lambda x: abs(x-1), graph[sx+i][sy:sy+3]))

def is_diff():
    for i in range(n):
        for j in range(m):
            if graph[i][j] != goal[i][j]:
                return True
    return False

n, m = MIS()
res = 0
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
goal = [list(map(int, list(input().rstrip()))) for _ in range(n)]

for i in range(n-2):
    for j in range(m-2):
        if graph[i][j] != goal[i][j]:
            reverse(i, j)
            res += 1

print(-1 if is_diff() else res)