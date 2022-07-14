#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def trace(here):
    if here == -1:
        return None
    
    trace(s[here])
    print(a[here], end=' ')
    
    return None

n = int(input())
a = list(MIS())
# dp[i] := 수열에서 i번째 수를 포함하는 가장 긴 증가하는 부분수열의 길이
# 겹치는 부분문제 파악 : dp[i]는 dp[j] + 1 where j < i 
# hence a[j] < a[i]
dp = [1 for _ in range(n)]
s = [-1 for _ in range(n)]

for i in range(n):
    for j in range(i + 1):
        if a[j] < a[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            s[i] = j
res = max(dp)

print(res)
trace(dp.index(res))