#-*- coding:utf-8 -*-
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = sorted([int(input()) for _ in range(n)])
max_weight = arr[-1]

for size in range(1, n+1):
    max_weight = max(max_weight, size * arr[-size])
    
print(max_weight)