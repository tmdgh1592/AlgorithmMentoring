#dp[i][j] =: 정수 i를 j개의 숫자로 나타내는 가짓수
import sys
MOD = int(1e9)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = list(MIS())
dp = [[0] * (n[1] + 1) for i in range(n[0] + 1)]
