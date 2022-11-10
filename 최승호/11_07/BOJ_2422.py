#-*- coding:utf-8 -*-
import sys
from collections import defaultdict
from itertools import combinations

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def is_banned(comb):
    for val in comb:
        for ban in banneds[val]:
            if ban in comb: return True
    return False


n, m = MIS()
banneds = defaultdict(list)
res = 0

for _ in range(m):
    a, b = MIS()
    banneds[a].append(b)
    banneds[b].append(a)

for sub in list(combinations(range(1,n+1), 3)):
    if not is_banned(sub): res+= 1
    
print(res)