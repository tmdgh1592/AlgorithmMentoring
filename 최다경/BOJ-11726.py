n = int(input())
dp = [0] * 10001

def dpf(dp, n):
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

dpf(dp, n)
print(dp[n])