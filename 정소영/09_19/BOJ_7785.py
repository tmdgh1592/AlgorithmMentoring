#-*- coding:utf-8 -*-
from collections import defaultdict
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
data = defaultdict(list)

for _ in range(n):
    name, report = input().rstrip().split()
    data[name].append(report)

res = list()
for name in data:
    if data[name][-1] == "enter":
        res.append(name)

print(*sorted(res, reverse=True), sep='\n')