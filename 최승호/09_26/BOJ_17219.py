#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
mdict = {}

for _ in range(n):
    key, val = input().rstrip().split()
    mdict[key] = val

for _ in range(m):
    print(mdict[input().rstrip()])