n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dp = [10001] * (n + 1) 
dp[0] = 0
dp[1] = arr[1]


for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - j] + arr[j])

print(dp)

print(dp[n])


