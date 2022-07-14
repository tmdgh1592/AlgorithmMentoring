#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
a = list(MIS())

# dp[i] := 수열에서 i번째 수를 포함하는 합
# dp[i]를 구하려면 2가지 경우가 존재한다
# 1. dp[i - 1] + a[i]
# 2. a[i]
dp = [0 for _ in range(n)]
dp[0] = a[0]

for i in range(1, n):
    dp[i] = max(dp[i - 1] + a[i], a[i])

print(max(dp))