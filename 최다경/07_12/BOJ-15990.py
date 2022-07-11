# n = int(input())
# arr = []
# MOD = int(1e9) + 9
# for i in range(n):
#     arr.append(int(input()))


# dp = [[0] * 4 for _ in range(100001)]

# def dpf(t):
#     for i in range(1, t + 1):
#         if i >= 1:
#             dp[i][1] = dp[i - 1][2] + dp[i - 1][3]
#             if i == 1:
#                 dp[i][1] = 1
#         if i >= 2:
#             dp[i][2] = dp[i - 2][1] + dp[i - 2][3]
#             if i == 2:
#                 dp[i][2] = 1
#         if i >= 3:
#             dp[i][3] = dp[i - 3][1] + dp[i - 3][2]
#             if i == 3:
#                 dp[i][3] = 1
#     return (dp[t][1] + dp[t][2] + dp[t][3]) % MOD

     

# for i in arr:
#     print(dpf(i))

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
# dp = [[0] * 4 for _ in range(100001)]

# def dpf(t):
#     for i in range(1, t + 1):
#         if i >= 1:
#             dp[i][1] = dp[i - 1][2] + dp[i - 1][3]
#             if i == 1:
#                 dp[i][1] = 1
#         if i >= 2:
#             dp[i][2] = dp[i - 2][1] + dp[i - 2][3]
#             if i == 2:
#                 dp[i][2] = 1
#         if i >= 3:
#             dp[i][3] = dp[i - 3][1] + dp[i - 3][2]
#             if i == 3:
#                 dp[i][3] = 1
#     return (dp[t][1] + dp[t][2] + dp[t][3]) % MOD

     

# for i in arr:
#     print(dpf(i))
print(list(MIS), n)