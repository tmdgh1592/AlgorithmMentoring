n = int(input())
MIS = lambda: map(int, input().rstrip().split())
table = [list(MIS()) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    if i + table[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + table[i][0]] + table[i][1])
print(dp[0])