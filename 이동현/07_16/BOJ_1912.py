#dp[i][i] =: dp[i]를 마지막으로 하는 가장 큰 연속합
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
numbers =list(MIS())
max =  0

dp = [[0]*2 for i in range(n)]
for i in range(n):
    dp[i][0] = numbers[i]
dp[0][1] = dp[0][0]
max = dp[0][1]

for i in range(1, n):
    if dp[i - 1][1] > 0:
        dp[i][1] = dp[i][0] + dp[i - 1][1]
    else:
        dp[i][1] = dp[i][0]
    if max < dp[i][1]:
        max = dp[i][1]
print(max)