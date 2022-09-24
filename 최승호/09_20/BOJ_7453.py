# -*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
cnt = 0

A, B, C, D = [], [], [], []
AB = {}

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for a in A:
    for b in B:
        if (a+b) in AB:
            AB[a+b] += 1
        else:
            AB[a+b] = 1

for c in C:
    for d in D:
        if -(c+d) in AB:
            cnt += AB[-(c+d)]

print(cnt)