#시간 초과;;
MOD = int(1e9) + 9
n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))
dp = [[0]*3 for n in range(int(1e5) + 1)]
dp[1][0] = 1
dp[2][1] = 1
dp[3][0] = 1
dp[3][1] = 1
dp[3][2] = 1

max_num = max(num_list)

if max_num > 3:
    for i in range(4, max_num + 1):
        dp[i][0] = dp[i - 1][1] + dp[i - 1][2]
        dp[i][1] = dp[i - 2][0] + dp[i - 2][2]
        dp[i][2] = dp[i - 3][0] + dp[i - 3][1]
        
for i in num_list:
    print(sum(dp[i]) % MOD)