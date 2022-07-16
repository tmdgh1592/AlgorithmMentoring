# n = 1001
# cache[1001]
# A[1001]
# cache[-1] = float('inf')

# def lis(start):
#     if cache[start + 1] != -1:
#         return cache[start + 1]

#     cache[start + 1] = 1
#     for next in range(start + 1, n):
#         if A[start] < A[next]:
#             cache[start + 1] = max(1 + lis(next), cache[start + 1])
#     return cache[start + 1]

#     res = 0
#     lis(-1)

# dp[i] = A[1], A[2], ..., A[i] 까지 수열이 있을때, 
# A[i]를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이
# dp[i]는 반드시 A[i]를 포함

# A[a], A[b], ..., A[j], A[i]
# A[j] < A[i]
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
A = list(MIS())
dp = [1 for _ in range(n)]
dp[0] = 1

for i in range(n):
    for j in range(i):
        if A[j] < A[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))
