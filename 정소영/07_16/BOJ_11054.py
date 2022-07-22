#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = list(MIS())

dp = [0] * (n) 
dp1 = [0] * (n) # arr[i]부터 시작하는 가장 긴 감소하는 부분수열의 길이

#가장 긴 증가하는 부분 수열
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1 

#가장 긴 감소하는 부분 수열
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if arr[i] > arr[j] and dp1[i] < dp1[j]:
            dp1[i] = dp1[j]
    dp1[i] += 1 

for i in range(n):
    dp[i] += dp1[i] - 1 #중복되는 값 -1

print(max(dp))