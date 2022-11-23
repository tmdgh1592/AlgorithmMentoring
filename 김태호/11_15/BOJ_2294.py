import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, k = MIS()
data = [int(input()) for _ in range(n)]
dp = [float('inf') for _ in range(k + 1)]

# dp[k] := k원이 되도록 하는 동전의 최소 개수
# 2293과 논리 비슷

dp[0] = 0

for i in range(n):
    for j in range(data[i], k + 1):
        dp[j] = min(dp[j], dp[j - data[i]] + 1)

print(dp[k] if dp[k] != float('inf') else -1)