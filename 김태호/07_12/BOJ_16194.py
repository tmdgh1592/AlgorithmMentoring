#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
p = [0] + list(MIS())
dp = [-1 for _ in range(n + 1)]
dp[0] = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if dp[i] == -1 or dp[i] > dp[i - j] + p[j]:
            dp[i] = dp[i - j] + p[j]

print(dp[n])
