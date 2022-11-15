#dp[i] := i번째 칸까지 가는데 걸리는 점프의 최소

import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
dist = list(MIS())
dp = [n + 1] * n
dp[0] = 0
cnt = 0
for i in range(n):
    for j in range(1, dist[i] + 1):
        if i + j >= n: continue
        dp[i + j] = min(dp[i + j], dp[i] + 1)

if dp[-1] == n + 1: print(-1)
else: print(dp[-1])