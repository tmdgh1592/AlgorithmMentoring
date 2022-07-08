#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

dp = [0] * (int(1e6) + 1)
n = int(input())

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if not i % 2: dp[i] = min(dp[i], dp[i // 2] + 1)
    if not i % 3: dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])