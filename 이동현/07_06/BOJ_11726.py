# dp[i] = dp[i-2] + 2
# dp[i] = dp[i] + 1
n = int(input())
MOD = int(1e4) + 7
dp = [0] * (int(1e3) + 1)
dp[1] = 1
dp[2] = 2
for i in range(1, n+1):
    if i <= 2:
        continue
    dp[i] = dp[i - 2] + dp[i - 1]
    dp[i] %= MOD
print(dp[i])
