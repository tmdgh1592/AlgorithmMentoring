import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
dp = [float('inf')] * (n + 1)
dp[0] = 0
dp[1] = 1

if n <= 1:
    print(dp[n])
    exit()

for i in range(2, n + 1):
    j = 0
    while(i >= j * j):
        res = min(dp[i - 1] + 1, dp[i - j * j] + 1)
        dp[i] = min(res, dp[i])
        # print(i, dp, j)
        j += 1


print(dp[n])