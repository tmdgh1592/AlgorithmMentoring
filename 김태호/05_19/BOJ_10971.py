#-*- coding:utf-8 -*-
import sys
from itertools import permutations

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
INF = 987654321

n = int(input())
cost = [list(MIS()) for _ in range(n)]

res = INF

# for perm in permutations(range(n), n):
#     tmp = 0
#     for i in range(n - 1):
#         tmp += cost[perm[i]][perm[i + 1]]
#     tmp += cost[perm[-1]][perm[0]]
    
#     res = min(tmp, res)
    
# print(res)

for perm in permutations(range(1, n), n - 1):
    tmp = 0
    for i in range(n - 2):
        if cost[perm[i]][perm[i + 1]] == 0:
            tmp = INF
            break
        tmp += cost[perm[i]][perm[i + 1]]
    
    if cost[0][perm[0]] and cost[perm[-1]][0]:
        tmp += cost[0][perm[0]]
        tmp += cost[perm[-1]][0]
    else:
        continue
    
    res = min(tmp, res)
    
print(res)