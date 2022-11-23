import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, k = MIS()
coin = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)
#dp[i] = i원을 만들 수 있는 경우의 수
dp[0] = 1

for i in range(n):
    for j in range(coin[i], k + 1):
        dp[j] += dp[j - coin[i]]

print(dp[k])