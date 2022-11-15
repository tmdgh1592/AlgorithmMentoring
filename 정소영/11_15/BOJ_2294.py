#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, k = MIS()
arr = [int(input()) for _ in range(n)]

dp = [float('inf') for _ in range(k + 1)] 
#dp[k] = k원이 되도록하는 최소 동전 사용 수

dp[0] = 0

for i in arr:
    for j in range(i, k + 1):
            dp[j] = min(dp[j], dp[j - i] + 1)
            
print(-1 if dp[k] == float('inf') else dp[k])