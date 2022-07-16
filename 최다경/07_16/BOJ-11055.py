import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
A = list(MIS())
dp = A.copy()
dp[0] = A[0]
for i in range(n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[j] + A[i], dp[i])
print(max(dp))
print(dp)

