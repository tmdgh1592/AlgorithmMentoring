# dp[i] := i원을 만들 수 있는 경우의 수
import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, k = MIS()
coin = list()
for i in range(n):
    coin.append(int(input()))

dp = [0 for _ in range(k + 1)]

dp[0] = 1

for i in coin:
    for j in range(i, k + 1):
        if dp[j - i] > 0:
            dp[j] += dp[j - i]

print(dp)
print(dp[k])