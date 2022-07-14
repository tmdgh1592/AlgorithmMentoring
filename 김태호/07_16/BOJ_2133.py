#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3

for i in range(4, n + 1, 2):
    dp[i] = 2 + dp[i - 2] * 3 + sum(dp[:i - 2]) * 2

print(dp[n])
