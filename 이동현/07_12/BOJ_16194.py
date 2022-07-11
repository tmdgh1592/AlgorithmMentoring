MIS = lambda: map(int, input().rstrip().split())
n = int(input())
cost = [0] + list(MIS())
MAX = int(1e8)
dp = [MAX]*(int(1e3) + 1)
dp[0] = 0
dp[1] = cost[1]
for i in range(1, n+ 1):
    for j in range(1, n+1):
        if j > i:
            break
        dp[i] = min(dp[i], dp[i - j] + cost[j])
print(dp[i])