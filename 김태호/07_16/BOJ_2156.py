#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())


data = [int(input()) for _ in range(int(input()))]
dp = [0 for _ in range(len(data))]

dp[0] = data[0]
if len(data) > 1:
    dp[1] = data[0] + data[1]
for i in range(2, len(data)):
    dp[i] = max(dp[i - 1], dp[i - 2] + data[i], dp[i - 3] + data[i] + data[i - 1])

print(dp[-1])