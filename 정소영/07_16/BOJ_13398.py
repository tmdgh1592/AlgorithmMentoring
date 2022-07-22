#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = list(MIS())

dp = [0 for _ in range(n)]
dp1 = [0 for _ in range(n)]

dp[0] = dp1[0] = arr[0]

for i in range(1,n):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])
    dp1[i] = max(dp[i - 1], dp1[i - 1] + arr[i])

print(max(max(dp,dp1)))