n = int(input())
dp = [[0]*10 for _ in range(n+1)]
MOD = int(1e9)

for i in range(1,10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0: #앞이 0이 나오면 뒤에 1만
            dp[i][j] = dp[i-1][1]
        elif j == 9: #앞이 9면 뒤에 8만
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 
print(sum(dp[n]) % MOD)
