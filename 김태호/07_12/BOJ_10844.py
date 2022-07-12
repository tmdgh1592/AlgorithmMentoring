#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
MOD = int(1e9)

n = int(input())
dp = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j - 1 >= 0: dp[i][j] += dp[i - 1][j - 1];
        if j + 1 <= 9: dp[i][j] += dp[i - 1][j + 1];
        dp[i][j] %= MOD
        
print(sum(dp[n]) % MOD)