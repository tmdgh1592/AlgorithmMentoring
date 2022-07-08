#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())

dp = [0] * (n+1) #최소값

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1 # 1 횟수 추가 (-1에 대한 것)
    if i % 3 == 0 :
        dp[i] = min(dp[i // 3] + 1,dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1,dp[i])

print(dp[n])
