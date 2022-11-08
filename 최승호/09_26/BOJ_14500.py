#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
graph = [list(MIS()) for _ in range(n)]

shapes = [[[1, 1],[0, 1],[0, 1]],
         [[1, 1],[1, 0],[1, 0]],
         [[1, 0],[1, 0],[1, 1]],
         [[0, 1],[0, 1],[1, 1]],
         [[1, 1, 1],[1, 0, 0]],
         [[1, 1, 1],[0, 0, 1]],
         [[1, 0, 0],[1, 1, 1]],
         [[0, 0, 1],[1, 1, 1]],
         [[1, 1],[1, 1]],
         [[1, 1, 1, 1]],
         [[1],[1],[1],[1]],
         [[1, 0],[1, 1],[0, 1]],
         [[0, 1],[1, 1],[1, 0]],
         [[0, 1, 1],[1, 1, 0]],
         [[1, 1, 0],[0, 1, 1]],
         [[1, 1, 1],[0, 1, 0]],
         [[0, 1, 0],[1, 1, 1]],
         [[1, 0],[1, 1],[1, 0]],
         [[0, 1],[1, 1],[0, 1]]]

res = 0
for shape in shapes:
    garo = len(shape[0])
    sero = len(shape)
    for i in range(n - sero + 1):
        for j in range(m - garo + 1):
            temp = 0
            for a in range(sero):
                for b in range(garo):
                    temp += graph[i+a][j+b] * shape[a][b]
            res = max(res, temp)

print(res)