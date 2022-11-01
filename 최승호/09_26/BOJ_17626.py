#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
dp = [4] * (n + 1)
dp[0], dp[1] = 0, 1

for num in range(2, n+1):
    i, min_cnt = 1, 4
    while i**2 <= num:
        min_cnt = min(min_cnt, dp[num - i**2] + 1)
        i += 1
    dp[num] = min_cnt 

print(dp[n])