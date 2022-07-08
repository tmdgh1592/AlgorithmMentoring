#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
p = list(MIS())
p.insert(0,0)

dp = [0] * (n+1)

# dp[1] = p[1], dp[2] = dp[1] + p[1] or dp[0] + p[2] ... dp[i] = dp[i-j] + p[j]

for i in range(1,n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i],dp[i-j]+p[j]) 
        
print(dp[n])
