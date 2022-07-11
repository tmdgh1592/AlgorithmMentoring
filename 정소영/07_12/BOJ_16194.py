#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
p = list(MIS())
p.insert(0,0)

dp = [False] * (n+1) 

for i in range(1,n + 1):
    for j in range(1, i + 1):
        if dp[i] == False:
            dp[i] = dp[i-j] + p[j]
        else:
            dp[i] = min(dp[i], dp[i-j]+p[j]) 
        
print(dp[n])
