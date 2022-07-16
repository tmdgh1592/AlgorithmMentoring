n, m = map(int, input().split())
MOD = int(1e9)
dp = [1 for _ in range(n + 1)]

#dp[i] :=  / dp는 이전단계의 현재 index에 해당하는 수 + 현재단계의 이전 index에 해당하는 수
dp[0] = 1
for i in range(m - 1):
    for j in range(1, n + 1):
        dp[j] += dp[j-1]

print(dp[-1] % MOD)