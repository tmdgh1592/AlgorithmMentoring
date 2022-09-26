#-*- coding:utf-8 -*-
import sys
from collections import Counter
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
data = Counter(filter(lambda x : len(x) >= m, [input().rstrip() for _ in range(n)]))
print(*list(map(lambda x : x[0], sorted(data.items(), key=lambda x : (-x[1], -len(x[0]), x[0])))), sep='\n')
