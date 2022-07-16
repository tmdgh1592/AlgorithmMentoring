import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

MOD = int(1e9) + 9
dp = [0 for _ in range(int(1e6) + 1)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, int(1e6) + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD


for _ in range(int(input())):
    print(dp[int(input())])

#메모리 초과, 엔터 단위 배열 만드는 법?

