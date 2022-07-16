import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
A = list(MIS())

dp = [1 for _ in range(n)]
dp[0] = 1

for i in range(n):
    for j in range(i):
        print(i, j, A[j], A[i])
        if A[j] > A[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            print('dp', dp[i])

print(dp)