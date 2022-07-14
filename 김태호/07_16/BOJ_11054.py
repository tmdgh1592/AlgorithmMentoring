#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
a = list(MIS())
dp1 = [1 for _ in range(n)]
dp2 = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[j] < a[i] and dp1[i] < dp1[j] + 1:
            dp1[i] = dp1[j] + 1

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if a[j] < a[i] and dp2[i] < dp2[j] + 1:
            dp2[i] = dp2[j] + 1

print(max([dp1[i] + dp2[i] - 1 for i in range(n)]))
