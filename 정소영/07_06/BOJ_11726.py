#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())

dp = [0] * (n + 1) #2 * N의 경우의 수

#런타임 에러
# dp[1] = 1 # 2 * 1 -> 1
# dp[2] = 2 # 2 * 2 -> 2
if n <= 2:
    print(n)
else:
    dp[1] = 1
    dp[2] = 2
        
    for i in range(3,n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n]%10007)

