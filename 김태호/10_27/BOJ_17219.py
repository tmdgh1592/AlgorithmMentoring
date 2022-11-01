#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
data = dict()

for _ in range(n):
    k, v = input().rstrip().split()
    data[k] = v
for _ in range(m):
    print(data[input().rstrip()])
