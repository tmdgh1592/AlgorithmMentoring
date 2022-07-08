#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

MOD = int(1e4) + 7

dp = [0] * (int(1e3) + 1)
dp[1] = 1
dp[2] = 2
n = int(input())

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= MOD

print(dp[n])