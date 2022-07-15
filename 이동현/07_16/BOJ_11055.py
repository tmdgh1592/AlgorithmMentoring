# dp[i][j] =: dp[i][j]는 dp[i]로 끝나는 증가 부분 순열의 최대 합이다.
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
numbers =list(MIS())
temp = 0
dp = [[0]*2 for i in range(n)]
for i in range(n):
    dp[i][0] = numbers[i]
dp[0][1] = dp[0][0]
max = dp[0][1]
for i in range(1, n):
    for j in range(i):
        if dp[i][0] <= dp[j][0]:
            continue
        else:
            if temp < dp[j][1]:
                temp = dp[j][1]
    dp[i][1] = temp + dp[i][0]
    if dp[i][1] > max:
        max= dp[i][1]
    temp = 0

print(max)