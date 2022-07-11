number = int(input())
dp = [0] * (int(1e6) + 1)
def func():
    for i in range(2, number+1):
        dp[i] = dp[i - 1] +1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
func()
print(dp[number])