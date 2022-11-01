#-*- coding:utf-8 -*-
import sys
from collections import defaultdict
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
d = defaultdict(set)

for _ in range(m):
    u, v = MIS()
    d[u].add(v)
    d[v].add(u)

res = float('inf')

for i in range(1, n + 1):
    for j in d[i]:
        for k in d[j]:
            if i in d[k]:
                res = min(len(d[i]) + len(d[j]) + len(d[k]) - 6, res)


print(res if res != float('inf') else -1)