# dp[i][j] := i, j가 선택 되었을 때 최대 합
# i, j가 선택되기전에 선택된 수는 i - 1, j or i - 1, j - 1
import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())

lst = [list(MIS()) for _ in range(n)]
dp = [[0 for _ in range(len(lst))] for _ in range(len(lst))]
dp[0][0] = lst[0][0]

for i in range(1, n):
    for j in range(i + 1):
        print(i, j)
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + lst[i][j]

print(max(dp[-1]))
