#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
lst = [list(MIS()) for _ in range(n)]

dp = [0] * (len(lst) + 1) #최대값

for i in range(n - 1, -1, -1):
    if i + lst[i][0] > n :
        dp[i] = max(dp[i], dp[i + 1])
    else :
        dp[i] = max(dp[i + 1], dp[i + lst[i][0]] + lst[i][1])

print(dp[0])