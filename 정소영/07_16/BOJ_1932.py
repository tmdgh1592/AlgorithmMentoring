#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = [list(MIS()) for _ in range(n)]
dp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]

dp[0][0] = arr[0][0]

for i in range(1,len(arr)):
    for j in range(i + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + arr[i][j]

print(max(dp[-1]))

# for i in range(1,n):
#     for j in range(len(arr[i])):
#         if j == 0 :
#             arr[i][j] += arr[i- 1][j]
#         elif j == i:
#             arr[i][j] += arr[i - 1][j - 1]
#         else:
#             arr[i][j] += max(arr[i - 1][j], arr[i - 1][j - 1])

# print(max(arr[n-1]))