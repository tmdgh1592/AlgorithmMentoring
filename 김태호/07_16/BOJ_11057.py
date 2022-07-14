#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
MOD = int(1e4) + 7

n = int(input())
# dp[i][j] := 길이가 i인 오르막 수 이때 마지막에 사용한 숫자는 j이다.

dp = [[0 for _ in range(10)] for _ in range(n + 1)]

for i in range(10):
    dp[1][i] = 1
    
for i in range(2, n + 1):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][k]
            dp[i][j] %= MOD
            
print(sum(dp[n]) % MOD)