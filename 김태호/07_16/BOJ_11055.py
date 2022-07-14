#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
a = list(MIS())
dp = [0 for _ in range(n)]

for i in range(n):
    dp[i] = a[i]
    for j in range(i):
        if a[j] < a[i] and dp[i] < dp[j] + a[i]:
            dp[i] = dp[j] + a[i]

print(max(dp))
