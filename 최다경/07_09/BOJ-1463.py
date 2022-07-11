n = int(input())
dp = [0] * (n + 1)

def dpf(n, dp):
    dp[0] = 0
    dp[1] = 0
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 3 == 0:
            dp[i] = min(dp[int(i // 3)] + 1, dp[i])
        if i % 2 == 0:
            dp[i] = min(dp[int(i // 2)] + 1, dp[i])

dpf(n, dp)
print(dp[n])
