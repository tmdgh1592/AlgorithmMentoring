#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
name = [input().rstrip() for _ in range(n)]
d = dict(zip(name, map(str, range(1, n + 1))))
d.update({v : k for k, v in d.items()})

for _ in range(m):
    print(d[input().rstrip()])