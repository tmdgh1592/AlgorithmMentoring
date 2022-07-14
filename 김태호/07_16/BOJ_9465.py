#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

for _ in range(int(input())):
    n = int(input())
    data = [list(MIS()) for _ in range(2)]
    # dp[i][j] := ith column에서 얻을 수 있는 최대 점수 이때 j는 sticker의 상태를 나타냄
    # j == 0 : sticker 선택 x
    # j == 1 : 위쪽 선택
    # j == 2 : 아래쪽 선택
    dp = [[0 for _ in range(3)] for _ in range(n)]
    
    dp[0][1] = data[0][0]
    dp[0][2] = data[1][0]
    
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1])
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + data[0][i]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + data[1][i]
        
    print(max(dp[-1]))
    