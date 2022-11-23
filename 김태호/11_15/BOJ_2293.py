import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, k = MIS()
data = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k + 1)]

# dp[k] := k원을 만드는 경우의 수
# k원을 만들려면 i원을 만드는 경우의 수를 조사해봄 (where i < k)
# i원을 만드는 경우의 수가 이미 존재한다고 가정
# i원에서 동전을 더해 k원을 만들어봄

dp[0] = 1

for i in range(n):
    for j in range(data[i], k + 1):
        dp[j] += dp[j - data[i]]

print(dp[k])