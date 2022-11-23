import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, k = MIS()
coin = [int(input()) for _ in range(n)]
dp = [float('inf')] * (k + 1)
dp[0] = 0
#dp[i] = i원을 만드는데 드는 가장 작은 동전의 수


for i in range(n):
    for j in range(coin[i], k + 1):
        dp[j] = min(dp[j], dp[j - coin[i]] + 1)
        
if dp[-1] == float('inf'): print(-1)
print(dp[-1])