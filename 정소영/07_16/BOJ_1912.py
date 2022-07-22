#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = list(MIS())
dp = [0 for _ in range(n)]

dp[0] = arr[0]

for i in range(1,n):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])
print(max(dp))
