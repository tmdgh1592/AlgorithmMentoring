#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
MOD = int(1e9)

n, k = MIS()
# dp[n][k] := 0 ~ n 까지의 정수 k개를 더해서 그 합이 n이 되는 경우의 수

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n + 1):
    for j in range(1, k + 1):
        for l in range(i + 1):
            dp[i][j] += dp[i - l][j - 1]
            dp[i][j] %= MOD

print(dp[n][k])