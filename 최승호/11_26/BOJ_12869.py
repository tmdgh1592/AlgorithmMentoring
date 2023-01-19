#-*- coding:utf-8 -*-
from itertools import permutations
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())    
INF = float('inf')

n = int(input())
data = list(MIS()) + [0] * 2
damage = list(permutations([9, 3, 1], 3))
cache=[[[INF for _ in range(61)] for _ in range(61)] for _ in range(61)]
cache[0][0][0] = 0

for i in range(61):
    for j in range(61):
        for k in range(61):
            for d1, d2, d3 in damage:
                if i - d1 <= 0: d1 = i
                if j - d2 <= 0: d2 = j
                if k - d3 <= 0: d3 = k
        
                cache[i][j][k] = min(cache[i][j][k], cache[i - d1][j - d2][k - d3] + 1)

print(cache[data[0]][data[1]][data[2]])