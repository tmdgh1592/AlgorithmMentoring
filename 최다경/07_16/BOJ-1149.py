import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(sys.stdin.readline())
arr = [list(MIS()) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n)]
#dp[i][j] := 전에 칠한 색이 j일때 i번째 집을 칠하는 가장 적은 비용(누적)
dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]

for i in range(1, n):
    dp[i][0] = arr[i][0] + min(dp[i - 1][1], dp[i - 1][2]) 
    dp[i][1] = arr[i][1] + min(dp[i - 1][0], dp[i - 1][2]) 
    dp[i][2] = arr[i][2] + min(dp[i - 1][0], dp[i - 1][1]) 

print(min(dp[n - 1]))