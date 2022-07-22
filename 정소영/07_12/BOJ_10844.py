#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())

dp = [[0] * 10 for _ in range(n+1)] 
#dp[i][j] = i 자리수에 
#           i자리 숫자일때 해당 숫자 앞에 올 수 있는 숫자 j

MOD = int(1e9)
#  1 자리수인 경우 0이 앞에 올 수 없으므로 1로 초기화
for i in range(1,10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0: # 0 앞에 올 수 있는 숫자는 1
            dp[i][j] = dp[i - 1][j + 1]
        elif j == 9: # 9 앞에 올 수 있는 숫자는 8 밖에 없음
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[n]) % MOD)
        
