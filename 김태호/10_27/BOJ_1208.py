#-*- coding:utf-8 -*-
from collections import defaultdict
from itertools import combinations
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, s = MIS()
half = n // 2
data = list(MIS())
res = 0
d = defaultdict(int)

for i in range(half + 1):
    for combi in combinations(data[:half], i):
        d[sum(combi)] += 1

for i in range(n - half + 1):
    for combi in combinations(data[half:], i):
        res += d[s - sum(combi)]
        
print(res if s else res - 1)

