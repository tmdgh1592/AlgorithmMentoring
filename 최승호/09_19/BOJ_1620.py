#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
mdict = {}

for i in range(1, n+1):
    name = input().rstrip()
    mdict[name], mdict[str(i)] = i, name

for _ in range(m):
    print(mdict[input().rstrip()])