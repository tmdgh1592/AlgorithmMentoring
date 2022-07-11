n = int(input())
dp = [[0] * 2 for _ in range(91)]

dp[1][0] = 0
dp[1][1] = 1
# dp[2][0] = 1
# dp[2][1] = 0
# dp[3][0] = 1
# dp[3][1] = 1
# if n > 3:
for i in range(2, n + 1):
    for j in range(0, 2):
        if j == 0:
            dp[i][j] = dp[i - 1][0] + dp[i - 1][1]
        elif j == 1:
            dp[i][j] = dp[i - 1][0]

print(dp[n][0] + dp[n][1])
