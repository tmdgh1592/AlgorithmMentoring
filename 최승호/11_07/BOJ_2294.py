#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, k = MIS()
coins = [int(input()) for _ in range(n)]
dp = [float('inf')] * (k+1) # i원을 만들 수 있는 최소 동전의 수
dp[0] = 0 # 앙 자명띠

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

print(-1 if dp[k]==float('inf') else dp[k])