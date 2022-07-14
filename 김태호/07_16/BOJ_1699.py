#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
# dp[i] := i를 제곱수로 나타내었을 때 필요한 항의 최소 개수
# i = x + y + z + ...
# 마지막 항이 어떤 숫자일까?
# 1인 경우 dp[i] = dp[j - 1] + 1
# 2인 경우 dp[i] = dp[j - 4] + 1

dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = i
    j = 1
    
    while j * j <= i:
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1
        j += 1
        
print(dp[n])