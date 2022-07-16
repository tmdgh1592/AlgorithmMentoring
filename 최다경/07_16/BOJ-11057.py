#dp[i][j] := 길이가 i이고, 마지막 수가 j인 오르막수의 개수
# n = int(input())

# dp = [1 for _ in range(10)]

# for i in range(n - 1):
#     for j in range(1, 10):
#         print(i, j)
#         dp[j] += dp[j - 1]

n = int(input())
MOD = int(1e4) + 7
dp = [1 for _ in range(10)]

#dp[i] := 길이가 n이고, dp[i]로 끝나는 오르막수 

for i in range(n-1):
    for j in range(1, 10):
        print(i, j)
        dp[j] += dp[j-1]
    print(dp)

sum = sum(dp)

print(sum % MOD)
print(dp)



