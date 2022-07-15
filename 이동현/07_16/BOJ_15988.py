#dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
num_list = []
dp = [0] * (int(1e6) + 1)
MOD = int(1e9) + 9
for i in range(n):
    num_list.append(int(input()))
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

m = max(num_list)

for i in range(4, m + 1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD

for i in num_list:
    print(dp[i])