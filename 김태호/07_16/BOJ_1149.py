#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())


data = [list(MIS()) for _ in range(int(input()))]
dp = [[0 for _ in range(3)] for _ in range(len(data))]

dp[0][0] = data[0][0]
dp[0][1] = data[0][1]
dp[0][2] = data[0][2]

for i in range(1, len(data)):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + data[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + data[i][1]
    dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + data[i][2]

print(min(dp[-1]))