#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, k = MIS()
arr = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k + 1)]

dp[0] = 1

for i in arr:
    for j in range(i, k + 1):
        dp[j] += dp[j - i]

print(dp[k])