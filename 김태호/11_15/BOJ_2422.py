#-*- coding:utf-8 -*-
from itertools import combinations
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
info = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
res = 0


for _ in range(m):
    a, b = MIS()
    info[a][b] = 1
    info[b][a] = 1

for combi in combinations(range(1, n + 1), 3):
    if info[combi[0]][combi[1]] or info[combi[0]][combi[2]] or info[combi[1]][combi[2]]: continue;
    res += 1

print(res)

