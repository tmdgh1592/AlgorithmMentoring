#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
MOD = int(1e9) + 9
dp = [[0] * 4 for _ in range(int(1e5) + 1)]

for i in range(1, int(1e5) + 1):
    if i >= 1:
        dp[i][1] = dp[i - 1][2] + dp[i - 1][3]
        if i == 1:
            dp[i][1] = 1
    
    if i >= 2:
        dp[i][2] = dp[i - 2][1] + dp[i - 2][3]
        if i == 2:
            dp[i][2] = 1
    
    if i >= 3:
        dp[i][3] = dp[i - 3][2] + dp[i - 3][1]
        if i == 3:
            dp[i][3] = 1
    
    dp[i][1] %= MOD
    dp[i][2] %= MOD
    dp[i][3] %= MOD
    
    
        

for _ in range(int(input())):
    print(sum(dp[int(input())]) % MOD)