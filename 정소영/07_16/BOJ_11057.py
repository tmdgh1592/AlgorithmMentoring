#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

MOD = int(1e4) + 7

n = int(input())

dp =[[0 for _ in range(10)] for _ in range(n + 1)]
#dp[i][j] : 길이가 i이면서, j로 끝나는 숫자 (쉬운계단 10844와 비슷함)

for i in range(10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][k]

print(sum(dp[n]) % MOD)

# dp = [1] * 10

# for i in range(1,n):
#     for j in range(1,10):
#         dp[j] += dp[j - 1]

# print(sum(dp) % MOD)
