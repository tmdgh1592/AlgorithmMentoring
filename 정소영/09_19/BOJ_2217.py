#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
weight = sorted([int(input()) for _ in range(n)], reverse=True)

res = list()
for i in range(n):
    res.append(weight[i] * (i + 1))
    
print(max(res))