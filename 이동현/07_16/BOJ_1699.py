# dp[i][j] =: i를 제곱수의 합으로 나타낼때 최소 개수

n = int(input())
dp = [i for i in range(n+1)]
dp[0] = 0
dp[1] = 1

for i in range(1, n + 1):
    for j in range(1, int(i**(1/2)) + 1):
        if dp[i] > dp[i - (j*j)] + 1:
            dp[i] = dp[i - (j*j)] + 1
print(dp[n])

#python3으로 하면 시간 초과, PyPy3로 하면 맞았습니다 ㅠ