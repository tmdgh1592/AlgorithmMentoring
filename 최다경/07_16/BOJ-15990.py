import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = []
MOD = int(1e9) + 9
for i in range(n):
    arr.append(int(input()))
ma = max(arr)

dp = [[0] * 4 for _ in range(100001)]


for i in range(1, ma + 1):
    if i >= 1:
        dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
        if i == 1:
            dp[i][1] = 1
    if i >= 2:
        dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD
        if i == 2:
            dp[i][2] = 1 
    if i >= 3:
        dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD
        if i == 3:
            dp[i][3] = 1

for i in arr:
    print((dp[i][1] + dp[i][2] + dp[i][3]))

