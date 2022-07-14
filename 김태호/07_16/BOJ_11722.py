#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
a = list(MIS())
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[j] > a[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))
