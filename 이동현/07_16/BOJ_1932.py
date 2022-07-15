#dp[i][j] =: i번째 열 j번째를 선택했을때의 최대 합
import code
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(MIS()))
dp = [[0]*n for i in range(n)]

dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = triangle[i][j] + dp[i - 1][0]
        if j == i:
            dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
print(max(dp[n - 1]))