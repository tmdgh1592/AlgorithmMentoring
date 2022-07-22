#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())

MOD = int(1e9) + 9

dp = [[0] * 4 for _ in range(int(1e5) + 1)]

#dp[i][j] : i = 정수 n을 구하는 경우의 수, j = 1,2,3 중 마지막으로 사용한 수
#dp[i][1] = dp[i - 1][2] + dp[i - 1][3] : 마지막으로 사용한 숫자는 1이므로 2, 3을 이용 할 수 있다 
#dp[i][2] = dp[i - 2][1] + dp[i - 2][3]

dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

for i in range(4, int(1e5) + 1):

    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD


for _ in range(n):
    m = int(input())
    print(sum(dp[m]) % MOD)

# for i in range(4, int(1e5) + 1):
# if i >= 1:
#     dp[i][1] = dp[i - 1][2] + dp[i - 1][3]
#     if i == 1:
#         dp[i][1] = 1