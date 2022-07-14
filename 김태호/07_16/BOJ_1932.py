#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

data = [list(MIS()) for _ in range(int(input()))]
dp = [[0 for _ in range(len(data))] for _ in range(len(data))]

dp[0][0] = data[0][0]

for i in range(1, len(data)):
    for j in range(i + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + data[i][j]
        
print(max(dp[-1]))
