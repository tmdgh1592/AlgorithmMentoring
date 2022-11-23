import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
data = list(MIS())
dp = [n + 1] * n
dp[0] = 0

for i in range(n):
    for j in range(1, data[i] + 1):
        if i + j < n:
            dp[i + j] = min(dp[i] + 1, dp[i + j])

if dp[n - 1] == n + 1:
    print(-1)
else:
    print(dp[n - 1])


