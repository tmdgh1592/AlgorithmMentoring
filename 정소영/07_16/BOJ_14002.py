#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
arr = list(MIS())

dp = [0] * (n)
lst = list()

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

num = max(dp)
for i in range(n - 1, -1, -1):
    if dp[i] == num:
        lst.append(arr[i])
        num -= 1
    
print(max(dp))
print(*lst[::-1])
    
    

