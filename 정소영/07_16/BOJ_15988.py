#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

dp = [0 for _ in range(int(1e6) + 1)]
MOD = int(1e9) + 9

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,int(1e6) + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

t = int(input())

for i in range(t):
    n = int(input())
    print(dp[n] % MOD)
