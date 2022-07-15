#dp[i][j] =: 길이가 i 이고, j로 끝나는 오르막 수의 갯수

n = int(input())
dp = [[0] * 10 for i in range(n + 1)]
MOD = (int(1e4) + 7)
dp[1] = [1,1,1,1,1,1,1,1,1,1]
for i in range(2, n + 1):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][k]

print((sum(dp[n]) - dp[n][0] + 1) % MOD)