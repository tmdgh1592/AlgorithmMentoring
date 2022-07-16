#dp[i] = i를 제곱수의 합으로 나타냈을 때, 필요한 항의 최소 개수
n = int(input())
MAX = float('inf')
dp = [MAX for _ in range(n + 1)]
dp[0] = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j**2 > i: break
        dp[i] = min(dp[i], dp[i - (j**2)] + 1)
print(dp[n])