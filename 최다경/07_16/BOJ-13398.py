import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
A = list(MIS())

# dp = [0] * n
# dp[0] = A[0]
# m = 0

# for k in range(-1, n, 1):
#     if k >= 0:
#         tmp = A[k]
#         A[k] = 0
#     for i in range(1, n):
#         dp[i] = max(dp[i - 1] + A[i], A[i])
#         m = max(max(dp), m)
#     if k >= 0:
#         A[k] = tmp
 
# print(m)

dp = [[0] * n for _ in range(2)]
print(dp)