#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = list(MIS())
# cache 사용하기
# def func(lst):

#     if len(lst) == 0:
#         return 0
#     ret = 0

#     for i in range(len(lst)):
#         lst2 = list()
#         for j in range(i + 1, len(lst)):
#             if lst[i] < lst[j]:
#                 lst2.append(lst[j])
#         ret = max(1 + func(lst2), ret)
#     return ret

# print(func(arr))

dp = [0] * (n) 

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))