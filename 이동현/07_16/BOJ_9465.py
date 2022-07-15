#동물원 문제와 비슷 대각선을 고르거나, 아님 이전에 아무것도 고르지 않는 경우의 수가 있다. 
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
case = int(input())
cost = [[],[]]

for i in range(case):
    n = int(input())
    for i in range(2):
        cost[i] = list(MIS())
    dp = [[0]* 3 for i in range(n)]
    dp[0][0] = cost[0][0]
    dp[0][1] = cost[1][0]
    dp[0][2] = 0
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + cost[0][i]
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + cost[1][i]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
    print(max(dp[n - 1]))