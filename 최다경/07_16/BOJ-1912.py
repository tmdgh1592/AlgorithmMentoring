# dp[i] = A[i]를 마지막으로 하는 가장 큰 연속 합

# A[i - 1]을 포함 할 수도 안할 수도 있음
# dp[i] = max(dp[i - 1] + A[i], A[i])

import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
A = list(MIS())

dp = [0] * n
dp[0] = A[0]

for i in range(1, n):
    dp[i] = max(dp[i - 1] + A[i], A[i])

print(dp)