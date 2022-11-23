# dp[i] := i라는 가치를 만들 수 있는 최소 코인 갯수
import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, k = MIS()
coin = list()
for i in range(n):
    coin.append(int(input()))

dp = [(k + 1) for _ in range(k + 1)]
for i in coin:
    if i < k: dp[i] = 1

for i in coin:
    for j in range(i, k + 1):
        if j - i > 0:
            dp[j] = min(dp[j], dp[j - i] + 1)
print(coin)

if dp[k] == k + 1: print(-1)
else: print(dp[k])
