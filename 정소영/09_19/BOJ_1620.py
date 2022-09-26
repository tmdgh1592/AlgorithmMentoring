#-*- coding:utf-8 -*-
from collections import defaultdict
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()

pokemon = defaultdict(list)
for index in range(1,n + 1):
    name = input().rstrip()
    pokemon[index].append(name)
    pokemon[name].append(index)

quest = [input().rstrip() for _ in range(m)]

for i in quest:
    if i.isdigit():
        print(*pokemon[int(i)])
    else:
        print(*pokemon[str(i)])