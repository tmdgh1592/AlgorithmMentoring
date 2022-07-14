#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
MOD = 9901

n = int(input())
# dp[i][k] := i번째 줄에 사자를 배치하는 경우의 수 이때 k는 사자의 위치상태를 나타냄
# dp[i][0] := i번째 줄에 사자를 배치하지 않음
# dp[i][1] := i번째 줄에 사자를 왼쪽에 배치함
# dp[i][2] := i번째 줄에 사자를 오른쪽에 배치함

dp = [[0 for _ in range(3)] for _ in range(n + 1)]

dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1

for i in range(2, n + 1):
    total = sum(dp[i - 1])
    dp[i][0] = total
    dp[i][1] = total - dp[i - 1][1]
    dp[i][2] = total - dp[i - 1][2]
    
    for j in range(3):
        dp[i][j] %= MOD
    
print(sum(dp[n]) % MOD)