#dp[i] =: i번째 와인을 선택할때(혹은 하지 않을 때) 최대로 마실 수 있는 포도주의 양
#현재 포도주를 마시거나 안마시는 경우. 현재 포도주를 먹으면 이전 포도주를 먹느 경우와 이전의 전 포도주를 먹는 경우 두가지가 있음. 총 세가지 경우 중의 최댓값 찾기
n = int(input())
wine = []
for i in range(n):
    wine.append(int(input()))
dp = [0] * n
dp[0] = wine[0]
if n > 1:
    dp[1] = wine[0] + wine[1]
if n > 2:
    dp[2] = max(wine[2] + wine[1], wine[2] + wine[0], dp[1])
if n > 3: 
    for i in range(3, n):
        dp[i] = max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i])
print(dp[n-1])